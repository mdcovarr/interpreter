
class Frame(object):
    def __init__(self, name, global_scope):
        self.name = name
        self.current_scope = None
        self.scopes = []
        self.scopes.append(self.current_scope)

    def add_scope(self):
        """
        Function used to add a new scope
        :return None:
        """

    def del_scope(self):
        """
        Function used to delete a scope
        :return:
        """

    def __contains__(self, key):
        """
        Function used to see if a current key value exists in the current scope
        :param key:
        :return:
        """