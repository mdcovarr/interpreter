from frame import Frame
from stack import Stack


class Memory(object):
    def __init__(self):
        self.GLOBAL_FRAME = Frame('global_mem', None)
        self.stack = Stack()

    def __setitem__(self, key, value):
        """
        Overload dict[key] = value function used to set value in the current scope
        :return None:
        """
        if self.stack.current_frame:
            in_scope = self.stack.current_frame.current_scope
        else:
            in_scope = self.GLOBAL_FRAME.current_scope

        curr_scope = in_scope
        while curr_scope and key not in curr_scope:
            curr_scope = curr_scope.parent

        if curr_scope:
            in_scope = curr_scope

        in_scope[key] = value



    def __getitem__(self, key):
        """
        Overload dict [] function used to get a value using a key, from the current scope
        :return:
        """
        pass

    def add_frame(self, new_frame_name):
        """
        Function used to add a new frame
        :param new_frame_name: new frame name
        :return None:
        """
        pass

    def del_frame(self):
        """
        Function used to delete the a frame from the stack
        :return None:
        """

    def add_scope(self):
        """
        function used to add a scope to the current frame
        :return:
        """

    def del_scope(self):
        """
        Funtion used to delete a scope from the current frame
        :return:
        """