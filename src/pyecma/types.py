
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
        return '<ECMAScript undefined>'


class NaN(AbstractType):

    def __repr__(self):
        return '<ECMAScript NaN>'


class Null(AbstractType):

    def __repr__(self):
        return '<ECMAScript Null>'


class Object(dict):
    
    def __init__(self, items):
        if isinstance(items, list):
            self.update(dict([(i.key, i.value,) for i in items]))
        else:
            self.update(items)
    
    def __call__(self, scope):
        di = dict()
        for k, v in self.items():
            di[k(scope)] = v(scope)
        return self.__class__(di)
    
    def __repr__(self):
        return '<ECMAScript Object <{%s}>>' % ', '.join(['%s: %s' % (repr(k),repr(v),) for k,v in self.items()])


class Array(Object):
    
    def __init__(self, items):
        if isinstance(items, list):
            self.update(dict([(Number(k), v,) for k, v in enumerate(items)]))
        else:
            self.update(items)
    
    def __repr__(self):
        return '<ECMAScript Array <[%s]>>' % ', '.join([repr(i) for i in self])

