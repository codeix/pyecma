from pyecma import types
from pyecma import exceptions


class Scope(dict):
    
    parent = None
    
    def __init__(self, parent):
        self.parent = parent
    
    def __setitem__(self, variable, value):
        create = isinstance(variable, Variable) and variable.create
        if str(variable) in self or self.parent is None or create:
            super(Scope, self).__setitem__(str(variable), value)
        else:
            self.parent[variable] = value

    def create(self, variable, value):
        super(Scope, self).__setitem__(str(variable), value)

    def setglobal(self, variable, value):
        if self.parent is None:
            self[variable] = value
        else:
            self.parent.set_global(variable, value)

    def get(self, variable):
        try:
            return self[variable]
        except exceptions.ReferenceError:
            return types.Undefinded()

    def __getitem__(self, variable):
        variable = str(variable)
        if not variable in self:
            if self.parent is None:
                raise exceptions.ReferenceError('%s is not defined' % variable)
            else:
                return self.parent[variable]
        return super(Scope, self).__getitem__(variable)


class Program(object):

    def __init__(self, ast):
        self.__dict__ = Scope(Scope(None))
        self.run(ast, self.__dict__)

    def run(self, statements, scope):
        for statement in statements:
            statement.prepare(scope)


class CodeBlock(Program):
    
    def __init__(self, ast):
        self.statements = ast
    
    def run(self, scope):
        for statement in self.statements:
            re = statement.prepare(scope)
            if re is not None:
                return re


class Operator(object):

    name = ''

    def __init__(self, func, name, parseint=False):
        self.func = func
        self.name = name
        self.parseint = parseint

    def __call__(self, scope, x, y):
        _class, x, y = self.autocasting(x(scope), y(scope))
        if self.parseint:
            try:
                return _class(self.func(int(x), int(y)))
            except TypeError:
                return types.Number(0)
        try:
            return _class(self.func(x, y))
        except TypeError:
            return types.NaN()
        
    def __repr__(self):
        return '<ECMAScript Operator a%sb>' % self.name
    
    def autocasting(self, x, y):
        if (isinstance(x, (types.String, types.Undefinded,)) or
            isinstance(y, (types.String, types.Undefinded,))):
            return types.String, types.String(str(x)), types.String(str(y))
        return types.Number, self.cast(x), self.cast(y)
    
    def cast(self, v):
        if isinstance(v, types.Bool):
            return types.Number(v and 1 or 0)
        elif isinstance(v, types.Null):
            return types.Number(0)
        else:
            return v


class Assign(Operator):

    def __repr__(self):
        return '<ECMAScript Assign x=%sb>' % self.name


class AssignSimple(Assign):

    def __init__(self):
        super(AssignSimple, self).__init__(lambda x,y: y, '=')

    def autocasting(self, x, y):
        return y.__class__, x, y


class Compare(Operator):

    def __init__(self, func, name, checktype=False):
        self.checktype = checktype
        super(Compare, self).__init__(func, name)

    def __repr__(self):
        return '<ECMAScript Compare x%sb>' % self.name

    def __call__(self, scope, x, y):
        if self.checktype:
            if type(x) == type(y):
                return types.Bool(True)
            else:
                return types.Bool(False)

        if (isinstance(x, types.String) + isinstance(y, types.String)) == 1:
            return types.Bool(False)

        if isinstance(y, types.String) and isinstance(x, types.String):
            return types.Bool(self.func(x, y))

        if not isinstance(x, types.Number):
            x = types.Number(x)

        if not isinstance(y, types.Number):
            y = types.Number(y)
        
        return types.Bool(self.func(x, y))


class Statement(object):
    
    def __init__(self, variable, assign, expression):
        self.variable = variable
        self.assign = assign
        self.expression = expression
        
    def __call__(self, scope):
        if self.expression is None:
            scope.set(self.variable, types.Undefinded())
        elif self.assign is None:
            self.expression(scope)
        else:
            re = scope.get(self.variable)
            re = self.assign(scope, re, self.expression(scope))
            scope[self.variable] = re

    def prepare(self, scope):
        return self(scope)


class IfStatement(Statement):
    
    def __init__(self, expression, ifblock, elseblock):
        self.expression = expression
        self.ifblock = ifblock
        self.elseblock = elseblock

    def __call__(self, scope):
        if self.expression(scope):
            return self.ifblock.run(scope)
        else:
            if self.elseblock is not None:
                return self.elseblock.run(scope)


class WhileStatement(Statement):
    
    def __init__(self, expression, codeblock):
        self.expression = expression
        self.codeblock = codeblock
        
    def __call__(self, scope):
        scope = Scope(scope)
        while self.expression(scope):
            re = self.codeblock.run(scope)
            if re is not None:
                return re


class DoWhileStatement(WhileStatement):

    def __call__(self, scope):
        scope = Scope(scope)
        while True:
            re = self.codeblock.run(scope)
            if re is not None:
                return re
            if not self.expression(scope):
                break


class ReturnStatement(Statement):
    
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, scope):
        return self.expression(scope)


class BreakStatement(ReturnStatement):

    def __init__(self):
        pass

    def __call__(self, scope):
        return types.Undefinded()


class Function(object):
    
    def __init__(self, ast):
        self.name = ast['name']
        self.code = ast['body']['code']
        sign = ast['body']['sign']
        if len(sign) is 2:
            sign = [sign[1]] + sign[0]
        self.signatur = sign
    
    def __call__(self, *args):
        scope = Scope(self.scope)
        for index, name in enumerate(self.signatur):
            if len(args) > index:
                scope.create(name, self.cast(args[index]))
            else:
                scope.create(name, types.Undefinded())
        scope.create('arguments', [self.cast(a) for a in args])
        return self.code.run(scope)
        
    def cast(self, value):
        if isinstance(value, str):
            return types.String(value)
        elif isinstance(value, (int, float,)):
            return types.Number(value)
        else:
            raise exceptions.ArgumentError('type was recognize for %s' % value)

    def prepare(self, scope):
        self.scope = scope
        scope[self.name] = self
    
    def __repr__(self):
        return '<ECMAScript Function %s>' % self.name


class Calculation(object):
    
    def __init__(self, ast):
        self.ast = ast

    def __call__(self, scope=None):
        if scope is None:
            scope = Scope(None)
        ex = [i for i in self.ast if not isinstance(i, list) or len(i)]
        if len(ex) is 1:
            return ex[0](scope)
        init, part = ex
        return self.cal(scope, init(scope), part)
        
        
    def cal(self, scope, init, part):
        part = zip([e for i,e in enumerate(part) if i%2 is 0 ],
                   [e for i,e in enumerate(part) if i%2 is 1 ])
        for op, dig in part:
            if isinstance(dig, list):
                dig, sub = dig
                init = op(scope, init, self.cal(scope, dig(scope), sub))
            else:
                init = op(scope, init, dig(scope))
        return init
    
    def __repr__(self):
        return '<ECMAScript Calculation <%s>>' % self.ast


class Callable(object):
    
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __call__(self, scope):
        function = scope[self.name]
        if not isinstance(function, Function):
            raise exceptions.TypeError('%s is not a function' % type(function))
        return function(*[p(scope) for p in self.params])


class Expression(object):

    def __init__(self, calculation, compares):
        self.calculation = calculation
        self.compares = compares
    
    def __call__(self, scope=None):
        re = self.calculation(scope)
        for comp in self.compares:
            re = comp.op(scope, re, comp.cal(scope))
        return re

    def __repr__(self):
        return '<ECMAScript Expression <%s %s>>' % (self.calculation, self.compares,)


class Variable(object):
    
    create = False
    
    def __init__(self, name):
        self.name = name

    def __call__(self, scope):
        return scope[self.name]

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<ECMAScript Variable <%s>>' % self.name

