
class AbstractType(object):

    def __call__(self, scope):
        return self


class Number(float, AbstractType):
    
    def __repr__(self):
        return '<ECMAScript Number <%s>>' % super(Number, self).__repr__()


class String(str, AbstractType):
    
    def __repr__(self):
        return '<ECMAScript String <%s>>' % super(String, self).__repr__()


class Bool(int, AbstractType):

    def __new__(cls, value):
        if isinstance(value, str):
            if value == 'true':
                value = True
            else:
                value = False
        return super(Bool, cls).__new__(cls, value)

    def __repr__(self):
        return '<ECMAScript Bool <%s>>' % (self and 'True' or 'False')


class Undefined(AbstractType):

    def __repr__(self):
        return '<ECMAScript Undefined>'


class NaN(AbstractType):

    def __repr__(self):
        return '<ECMAScript NaN>'


class Null(AbstractType):

    def __repr__(self):
        return '<ECMAScript Null>'


class Object(dict):
    
    def __init__(self, items):
        self.update(items)

    def __call__(self, scope):
        di = self.__class__([])
        for k, v in self.items():
            di[k(scope)] = v(scope)
        return di

    def __getitem__(self, name):
        builtins = self.builtins()
        if name in self:
            return super(Object, self).__getitem__(name)
        if name in builtins:
            return builtins[name]
        return Undefined()

    def __repr__(self):
        return '<ECMAScript Object <{%s}>>' % ', '.join(['%s: %s' % (repr(k),repr(v),) for k,v in self.items()])


class Array(Object):
    
    def __init__(self, items):
        self.update((Number(k), v,) for k, v in enumerate(items))

    def __iter__(self):
        for i in self.values():
            yield i

    def builtins(self):
        return dict(length=Number(len(self)))

    def __repr__(self):
        return '<ECMAScript Array <[%s]>>' % ', '.join(repr(i) for i in self.values())
