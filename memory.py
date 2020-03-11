
class Memory(object):
    def __init__(self):
        self.GLOBAL_FRAME = None
        self.stack = None

    def __setitem__(self):
        """
        Overload dict[key] = value function used to set value in the current scope
        :return None:
        """
        pass

    def __getitem__(self):
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