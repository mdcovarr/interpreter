
class Scope(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.values = {}

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def __setitem__(self, var, value):
        self.values[var] = value

    def __getitem__(self, var):
        return self.values[var]

    def __contains__(self, key):
        return key in self.values

    def __repr__(self):
        output = []
        output.append('{name}\n'.format(name=self.name))

        for key, value in self.values.items():
            output.append('{key}:{value}'.format(key=key, value=value))

        return '\n'.join(output)
