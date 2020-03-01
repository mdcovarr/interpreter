from .token import *

NEWLINE = '\n'

RESERVED_KEYWORDS = {
    'char': Token(CHAR, 'char'),
    'int': Token(INT, 'int'),
    'float': Token(FLOAT, 'float'),
    'double': Token(DOUBLE, 'double'),
    'if': Token(IF, 'if'),
    'else': Token(ELSE, 'else'),
    'for': Token(FOR, 'for'),
    'while': Token(WHILE, 'while'),
    'do': Token(DO, 'do'),
    'return': Token(RETURN, 'return'),
    'break': Token(BREAK, 'break'),
    'continue': Token(CONTINUE, 'continue'),
    'void': Token(VOID, 'void'),
}


class Lexer(object):
    def __init__(self, text):
        """
        Constructor for the Lexer class object
        :param text: text to be read and tokenized
        """
        self.text = text.replace('\\n', '\n')
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.line = 1

    def error(self, message):
        """
        Function used to output if there is an error message that occurs
        :param message:
        :return None:
        """
        # need to output Error message
        print('Error: {message}'.format(message=message))
        exit(1)

    def skip_white(self):
        """
        Function used to skip whitespaces
        :return None:
        """
        curr_char = self.current_char

        while (curr_char.isspace()) and (curr_char is not None):
            # check if newline
            if curr_char == NEWLINE:
                self.line += 1

            self.advance()
            curr_char = self.current_char

    def advance(self):
        """
        Function used to advance the position we are pointing to in the
        text to evaluate
        :return None:
        """
        self.pos += 1

        if (self.pos > len(self.text) -1):
            # We have reachec end of text
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
