from scope import Scope


class Frame(object):
    def __init__(self, name, global_scope):
        self.name = name
        self.current_scope = self.create_new_scope(name, global_scope)
        self.scopes = []
        self.scopes.append(self.current_scope)

    @staticmethod
    def create_new_scope(name, global_scope):
        """
        Helper function to create new scope
        :param name:
        :param global_scope:
        :return:
        """
        scope_name = '{0}_{1}'.format(name, 1)
        curr_scope = Scope(scope_name, global_scope)

        return curr_scope

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