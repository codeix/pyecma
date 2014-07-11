class Object(object):
    
    def __init__(self, items):
        self.items = dict([(i.key, i.value,) for i in items])
    
    def __call__(self, scope):
        return self
    
    def __repr__(self):
        return '<ECMAScript Object <{%s}>>' % ', '.join(['%s: %s' % (k,v,) for k,v in self.items.items()])


class Array(object):
    def __init__(self, items):
        self.items = items
    
    def __call__(self, scope):
        return self
    
    def __repr__(self):
        return '<ECMAScript Array <[%s]>>' % ', '.join(self.items)