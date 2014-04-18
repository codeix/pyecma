
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

    def __init__(self, value):
        if isinstance(value, str):
            if value == 'true':
                value = True
            else:
                value = False
        super(Bool, self).__init__(value)

    def __repr__(self):
        return '<ECMAScript Bool <%s>>' % self and 'True' or 'False'


class Undefinded(AbstractType):

    def __repr__(self):
        return '<ECMAScript undefinded>'


class NaN(AbstractType):

    def __repr__(self):
        return '<ECMAScript NaN>'


class Null(AbstractType):

    def __repr__(self):
        return '<ECMAScript Null>'

