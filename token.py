"""
    Class to hold type and values of Tokens for C Language
"""

""" Define Operations """
ADD = 'ADD'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'
MOD = 'MOD'
INC = 'INC'
DEC = 'DEC'

AND = 'AND'
OR = 'OR'
XOR = 'XOR'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
LT = 'LT'
GT = 'GT'
LE = 'LE'
GE = 'GE'
EQ = 'EQ'
NE = 'NE'

LOG_AND = 'LOG_AND'
LOG_OR = 'LOG_OR'
LOG_NEG = 'LOG_NEG'

ASSIGN = 'ASSIGN'
ADD_ASSIGN = 'ADD_ASSIGN'
SUB_ASSIGN = 'SUB_ASSIGN'
MUL_ASSIGN = 'MUL_ASSIGN'
DIV_ASSIGN = 'DIV_ASSIGN'
MOD_ASSIGN = 'MOD_ASSIGN'
LEFT_ASSIGN = 'LEFT_ASSIGN'
RIGHT_ASSIGN = 'RIGHT_ASSIGN'
AND_ASSIGN = 'AND_ASSIGN'
XOR_ASSIGN = 'XOR_ASSIGN'
OR_ASSIGN = 'OR_ASSIGN'


""" Extra Characters """
LBRACKET = 'LBRACKET'
RBRACKET = 'RBRACKET'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
COMMA = 'COMMA'
DOT = 'DOT'
SEMICOLON = 'SEMICOLON'
COLON = 'COLON'
HASH = 'HASH'
QUESTION_MARK = 'QUESTION_MARK'

""" If Statement """
IF = 'IF'
ELSE = 'ELSE'
ID = 'ID'
RETURN = 'RETURN'

""" Loop Statements """
WHILE = 'WHILE'
FOR = 'FOR'
DO = 'DO'
BREAK = 'BREAK'
CONTINUE = 'CONTINUE'

""" Define Variable types """
STRING = 'STRING'
CHAR = 'CHAR'
INT  = 'INT'
FLOAT = 'FLOAT'
DOUBLE = 'DOUBLE'
VOID = 'VOID'
CHAR_CONST = 'CHAR_CONST'
INTEGER_CONST = 'INTEGER_CONST'
REAL_CONST = 'REAL_CONST'

""" EOF """
EOF = 'EOF'


class Token(object):
    def __init__(self, value, token_type):
        """
        Token class constructor
        :param value: token value character
        :param token_type: type of character e.g. Integer, Bracket
        """
        self.value = value
        self.type = token_type

    def __str__(self):
        """
        Function used to create the token string
        :return token: token containing the type and value of the token
        """
        token = 'Token({type}. {value})'.format(type=self.type, value=repr(self.value))

        return token

    def __repr__(self):
        """
        Function used to get the token string representation of the object
        :return: token containing the type and value of the token
        """
        return self.__str__()
