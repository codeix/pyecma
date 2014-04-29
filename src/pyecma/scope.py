import pyecma
from pyecma import types
from pyecma import exceptions
from pyecma.builtins import apply_to_scope


class Scope(dict):
    
    parent = None
    
    def __init__(self, parent):
        self.parent = parent
    
    def __setitem__(self, variable, value):
        create = isinstance(variable, pyecma.elements.Variable) and variable.create
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
            return types.Undefined()

    def __getitem__(self, variable):
        variable = str(variable)
        if not variable in self:
            if self.parent is None:
                raise exceptions.ReferenceError('%s is not defined' % variable)
            else:
                return self.parent[variable]
        return super(Scope, self).__getitem__(variable)


class GlobalScope(Scope):

    def __init__(self):
        super(GlobalScope, self).__init__(None)
        apply_to_scope(self)
