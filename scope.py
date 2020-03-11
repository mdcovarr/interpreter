
class Scope(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.values = {}

    def set_parent(self, parent):
        """
        Function used to set the parent scope
        :param parent:
        :return None:
        """
        self.parent = parent

    def get_parent(self):
        """
        Function used to get the parent scope
        :return None:
        """
        return self.parent

    def __setitem__(self, key, value):
        """
        Function used to override dict[key] = value function of dictionary
        :param key:
        :param value:
        :return:
        """
        self.values[key] = value

    def __getitem__(self, var):
        """
        Function used to get value from dict
        :param var:
        :return: value from self.values dictionary
        """
        return self.values[var]

    def __contains__(self, key):
        return key in self.values
