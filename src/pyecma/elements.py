


class Operator(object):

    name = '-'

    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __call__(self, x, y):
        return Number(self.func(x(), y()))

    def __repr__(self):
        return '<ECMAScript Operator a%sb>' % self.name


class Expression(object):
    
    def __init__(self, ast):
        self.ast = ast

    def __call__(self):
        ex = [i for i in self.ast if not isinstance(i, list) or len(i)]
        if len(ex) is 1:
            return Number(ex[0]())
        init, part = ex
        return Number(self.cal(init(), part))
        
        
    def cal(self, init, part):
        part = zip([e for i,e in enumerate(part) if i%2 is 0 ],
                   [e for i,e in enumerate(part) if i%2 is 1 ])
        for op, dig in part:
            if isinstance(dig, list):
                dig, sub = dig
                init = op(init, self.cal(dig(), sub))
            else:
                init = op(init, dig())
        return init
    
    def __repr__(self):
        return '<ECMAScript Expression <%s>>' % self.ast


class Number(float):
    def __call__(self):
        return self
    
    def __repr__(self):
        return '<ECMAScript Number <%s>>' % super(Number, self).__repr__()