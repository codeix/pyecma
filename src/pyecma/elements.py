from pyecma import types
from pyecma import exceptions
from pyecma.scope import Scope
from pyecma.scope import GlobalScope
from pyecma.builtins import AbstractFunction


class Program(object):

    def __init__(self, ast):
        self.__dict__ = GlobalScope()
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
            if isinstance(re, tuple):
                val, stat = re
            else:
                val, stat = re, None
            if val is not None:
                return val, stat
        return val, stat


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


class Increment(object):
    
    def __init__(self, operation, variable, pre=True):
        self.operation = operation
        self.variable = variable
        self.pre = pre

    def __call__(self, scope):
        re = self.operation(scope, self.variable, types.Number(1))
        old = scope[self.variable]
        scope[self.variable] = re
        if self.pre:
            return re
        else:
            return old


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

    def returnbehavior(self, value, statement):
        if isinstance(statement, BreakStatement):
            return None
        return value, statement


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
            re, stat = self.codeblock.run(scope)
            if re is not None:
                return self.returnbehavior(re, stat)


class DoWhileStatement(WhileStatement):

    def __call__(self, scope):
        scope = Scope(scope)
        while True:
            re, stat = self.codeblock.run(scope)
            if re is not None:
                return self.returnbehavior(re, stat)
            if not self.expression(scope):
                break


class ForStatement(Statement):
    
    def __init__(self, variable, condition, expression, codeblock):
        self.variable = variable
        self.condition = condition
        self.expression = expression
        self.codeblock = codeblock
    
    def __call__(self, scope):
        scope = Scope(scope)
        if self.variable is not None:
            self.variable(scope)
        while True:
            re, stat = self.codeblock.run(scope)
            if re is not None:
                return self.returnbehavior(re, stat)
            if self.expression is not None:
                self.expression(scope)
            if self.condition is not None:
                if not self.condition(scope):
                    break


class SwitchStatement(Statement):
    
    hasdefault = False
    
    def __init__(self, expression, cases):
        self.expression = expression
        self.cases = cases
        c = len([i for i in cases if isinstance(i, SwitchCaseDefault)])
        if c > 1:
            raise exceptions.SyntaxError('More than one default clause in switch statement')

    def __call__(self, scope):
        scope = Scope(scope)
        comparevalue = self.expression(scope)
        checkmatch = False
        for case in self.cases:
            if checkmatch or isinstance(case, SwitchCase):
                if checkmatch or case.match(scope, comparevalue):
                    re, stat = case.run(scope)
                    checkmatch = True
                    if re is not None:
                        return self.returnbehavior(re, stat)

        if not checkmatch:
            for case in self.cases:
                if isinstance(case, SwitchCaseDefault):
                    return case.run(scope)


class SwitchCase(object):
    
    def __init__(self, expression, codeblock):
        self.expression = expression
        self.codeblock = codeblock
        self.compare = Compare(lambda x,y: x==y, '=')
    
    def match(self, scope, value):
        return self.compare(scope, value, self.expression(scope))
    
    def run(self, scope):
        return self.codeblock.run(scope)


class SwitchCaseDefault(object):
    
    def __init__(self, codeblock):
        self.codeblock = codeblock
    
    def match(self, scope, value):
        return True
    
    def run(self, scope):
        return self.codeblock.run(scope)
        

class ReturnStatement(Statement):
    
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, scope):
        return self.expression(scope), self


class BreakStatement(ReturnStatement):

    def __init__(self):
        pass

    def __call__(self, scope):
        return types.Undefinded(), self


class Function(AbstractFunction):
    
    def __init__(self, ast):
        self.name = ast['name']
        self.code = ast['body']['code']
        sign = ast['body']['sign']
        if len(sign) is 2:
            sign = [sign[1]] + sign[0]
        self.signatur = sign
    
    def __call__(self, *args):
        scope = Scope(self.scope)
        re = self.code.run(self.createscope(args, scope))
        if isinstance(re, tuple):
            re, stat = re
        return re

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
        if not isinstance(function, AbstractFunction):
            raise exceptions.TypeError('%s is not a function' % type(function))
        return function(*[p(scope) for p in self.params])


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




