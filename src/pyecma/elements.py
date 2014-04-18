from pyecma import exceptions



class Scope(dict):
    
    parent = None
    
    def __init__(self, parent):
        self.parent = parent
    
    def __setitem__(self, variable, value):
        if variable in self or self.parent is None:
            super(Scope, self).__setitem__(str(variable), value)
        else:
            self.parent[str(variable)] = value

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
            return Undefinded()

    def __getitem__(self, variable):
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
        super(CodeBlock, self).run(self.statements, scope)


class Operator(object):

    name = ''

    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __call__(self, scope, x, y):
        return Number(self.func(x(scope), y(scope)))

    def __repr__(self):
        return '<ECMAScript Operator a%sb>' % self.name


class Assign(Operator):

    def __repr__(self):
        return '<ECMAScript Assign x=%sb>' % self.name


class Statement(object):
    
    def __init__(self, variable, assign, expression):
        self.variable = variable
        self.assign = assign
        self.expression = expression
        
    def __call__(self, scope):
        if self.expression is None:
            scope.set(self.variable, Undefinded())
        elif self.assign is None:
            self.expression(scope)
        else:
            re = scope.get(self.variable)
            re = self.assign(scope, re, self.expression(scope))
            if self.variable.create:
                scope.create(self.variable, re)
            else:
                scope[self.variable] = re

    def prepare(self, scope):
        self(scope)


class Function(object):
    
    def __init__(self, ast):
        self.name = ast['name']
        self.create = ast['name'].create
        self.code = ast['body']['code']
        sign = ast['body']['sign']
        if len(sign) is 2:
            sign = [sign[1]] + sign[0]
        self.signatur = sign
    
    def __call__(self, *args):
        scope = Scope(self.scope)
        for index, name in enumerate(self.signatur):
            if len(args) > index:
                scope[name] = self.cast(args[index])
            else:
                scope[name] = Undefinded()
        scope['arguments'] = [self.cast(a) for a in args]
        self.code.run(scope)
        
    def cast(self, value):
        if isinstance(value, str):
            return String(str)
        elif isinstance(value, (int, float,)):
            return String(str)
        else:
            raise ArgumentError('type was recognize for %s' % arg)

    def prepare(self, scope):
        self.scope = scope
        if self.create:
            scope.create(self.name, self)
        else:
            scope[self.name] = self
    
    def __repr__(self):
        return '<ECMAScript Function %s>' % self.name


class Expression(object):
    
    def __init__(self, ast):
        self.ast = ast

    def __call__(self, scope=None):
        if scope is None:
            scope = Scope(None)
        ex = [i for i in self.ast if not isinstance(i, list) or len(i)]
        if len(ex) is 1:
            return Number(ex[0](scope))
        init, part = ex
        return Number(self.cal(scope, init(scope), part))
        
        
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
        return '<ECMAScript Expression <%s>>' % self.ast


class Number(float):
    def __call__(self, scope):
        return self
    
    def __repr__(self):
        return '<ECMAScript Number <%s>>' % super(Number, self).__repr__()


class String(str):
    def __call__(self, scope):
        return self
    
    def __repr__(self):
        return '<ECMAScript String <%s>>' % super(String, self).__repr__()


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


class Undefinded(object):

    def __call__(self, scope):
        return self

    def __repr__(self):
        return '<ECMAScript undefinded>'