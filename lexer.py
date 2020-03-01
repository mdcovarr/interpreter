from token import Token
from grammar import *

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

    def skip_single_comment(self):
        """
        Function used to ignore single comment line in text being analyzed
        and advance position
        :return None:
        """
        curr_char = self.current_char

        while curr_char is not None:
            if curr_char == NEWLINE:
                # done ignoring comment
                self.line += 1
                self.advance()
                return

            self.advance()
            curr_char = self.current_char

    def skip_block_comment(self):
        """
        Function used to ignore comment block in text being analyzed
        :return None:
        """
        curr_char = self.current_char

        while curr_char is not None:
            if curr_char == '*' and self.peek(1) == '/':
                self.advance()
                self.advance()
                return
            elif curr_char == NEWLINE:
                self.line += 1

            self.advance()

        error_message = 'Invalid Format, exiting...'
        self.error(error_message)

    def keyword(self):
        """
        Function used to handle if we see key work or some var
        :return token: Token created with value and type
        """
        val = ''

        while (self.current_char.isalpha()) and (self.current_char is not None):
            val += self.current_char
            self.advance()

        return RESERVED_KEYWORDS.get(val, Token(ID, val))

    def char(self):
        """
        Function used to handle chars between single quotes e.g., 'c'
        :return token: Return a char token
        """
        self.advance()
        char = self.current_char
        self.advance()

        if self.current_char != '\'':
            error_message = 'Invalid Char format!'
            self.error(error_message)

        self.advance()

        return Token(CHAR_CONST, ord(char))

    def string(self):
        """
        Function used to get string in double quotes in C language
        :return token: String token with value
        """
        string = ''
        self.advance()

        while self.current_char is not '"':
            if self.current_char is None:
                error_message = 'Invalid format for string!'
                self.error(error_message)

            string += self.current_char
            self.advance()

        self.advance()
        return Token(STRING, string)

    def number(self):
        """
        Function used to return numerical values such as integers, and doubles
        from text being analyzed
        :return token: INTEGER, FLOAT, DOUBLE .. numerical types
        """
         

    def peek(self, x):
        """
        Function used to peek forward from the current position self.pos by a value
        of x. e.g., self.pos + x
        :param x: check the self.pos + x character value
        :return val: the char value at position self.pos + x
        """
        if (self.pos + x) > len(self.text) - 1:
            # Index our of bounds
            return None
        else:
            val = self.text[self.pos + x]
            return val

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

    def get_next(self):
        """
        Function used to get the next char from the input text we want to analyze
        :return None:
        """

        while self.current_char is not None:

            if (self.current_char == '/') and (self.peek(1) == '/'):
                self.skip_single_comment()
                continue

            if (self.current_char == '/') and (self.peek(1) == '*'):
                self.skip_block_comment()
                continue

            if self.current_char.isspace():
                self.skip_white()
                continue

            if self.current_char.isalpha():
                # need to create var

            if self.current_char.isdigit():
                # need to create number

            if self.current_char == '"':
                # create string

            if self.current_char == '\'':
                # need to create char

