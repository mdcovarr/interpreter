"""
    Stack implementation utilized to keep track of different
    function calls. usage allows to keep track of scope when
    interpreting C code
"""
from frame import Frame


class Stack(object):
    """
    Stack implementation
    """
    def __init__(self):
        self.current_frame = None
        self.frames = []

    def add_frame(self, name, global_scope):
        """
        Function used to add a new frame
        :param name:
        :param global_scope:
        :return None:
        """
        curr_frame = Frame(name, global_scope)
        self.current_frame = curr_frame
        self.frames.append(self.current_frame)

    def del_frame(self):
        """
        Function used to delete a frame
        :return None:
        """
        self.frames.pop(len(self.frames) - 1)

        if len(self.frames) > 0:
            self.current_frame = self.frames[len(self.frames) - 1]
        else:
            self.current_frame = None
