import pyecma
from pyecma import types
from pyecma import exceptions


class AbstractFunction(object):
    
    signatur = tuple()
    
    def __call__(self, *args):
        raise NotImplemented('Need to subclass this class')

    def createscope(self, args, scope):
        for index, name in enumerate(self.signatur):
            if len(args) > index:
                scope.create(name, self.cast(args[index]))
            else:
                scope.create(name, types.Undefinded())
        scope.create('arguments', [self.cast(a) for a in args])
        return scope

    def cast(self, value):
        if isinstance(value, str):
            return types.String(value)
        elif isinstance(value, (int, float,)):
            return types.Number(value)
        else:
            raise exceptions.ArgumentError('type was recognize for %s' % value)

    def __repr__(self):
        return '<ECMAScript Builtin Function %s>' % self.__class__.__name__


class ParseInt(AbstractFunction):
    
    signatur = ('value',)
    
    def __call__(self, *args):
        scope = self.createscope(args, pyecma.scope.Scope(None))
        try:
            return types.Number(int(scope['value']))
        except ValueError:
            return types.Undefined()


def apply_to_scope(scope):
    scope['parseInt'] = ParseInt()
