from .token import *

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

