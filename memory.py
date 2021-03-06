"""
    Memory class utilized in order to create scope for c file being interpreted,
    and the functions encapsulated withing the interpreted file.

    Reference: https://github.com/SKantar/CInterpreter
"""

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
        if self.stack.current_frame:
            curr_scope = self.stack.current_frame.current_scope
        else:
            curr_scope = self.GLOBAL_FRAME.current_scope

        while curr_scope and key not in curr_scope:
            curr_scope = curr_scope.parent

        return curr_scope[key]

    def add_frame(self, new_frame_name):
        """
        Function used to add a new frame
        :param new_frame_name: new frame name
        :return None:
        """
        self.stack.add_frame(new_frame_name, self.GLOBAL_FRAME.current_scope)

    def del_frame(self):
        """
        Function used to delete the a frame from the stack
        :return None:
        """
        self.stack.del_frame()

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

    def declare_variable(self, key, value=None):
        """
        Function used to put newly declared varaible in scope
        :param key:
        :param value:
        :return:
        """
        if self.stack.current_frame:
            in_scope = self.stack.current_frame.current_scope
        else:
            in_scope = self.GLOBAL_FRAME.current_scope

        if value:
            in_scope[key] = value
        else:
            in_scope[key] = 0
