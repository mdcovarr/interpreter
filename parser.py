from grammar import *
from ast import *


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token

    def error(self, message):
        print('Error: {0}'.format(message))
        exit(1)

    def program(self):
        """
        Create the top level declaration of a program, e.g. a C file.
        :return Node: Program Node
        """
        root = Program(statements='', line='')
        return root

    def eat(self, token_type):
        """
        Function used to compare the current token type with passed token type.
        If type are equal, we 'eat' current token and assign the next token to current_token
        :param token_type: toke we are checking with current_token
        :return:
        """
        if token_type == self.current_token.type:
            self.current_token = self.lexer.get_next_token
        else:
            error_message = 'Error in token matching. exiting ...'
            self.error(error_message)

    def parse(self):
        """
        Top level function, when called, triggers parsing of C file
        :return Node: Program Node
        """
        node = self.program()

        if self.current_token.type != EOF:
            error_message = 'EOF not reached after parsing C file. exiting ...'
            self.error(error_message)

        return node
