
class Scope(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.values = {}
    
    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_value(self, var, value):
        self.values[var] = value
    
    def get_value(self, var):
        return self.values[var]

    def __repr__(self):
        output = []
        output.append('{name}\n'.format(name=self.name))

        for key, value in self.values.items():
            output.append('{key}:{value}'.format(key=key, value=value))
            
        return '\n'.join(output)