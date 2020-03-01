"""
    Class to hold type and values of Tokens for C Language
"""


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
        token = 'Token({type}. {value})'.format(type=self.type, value=self.value)

        return token

    def get_string(self):
        """
        Function used to get the token string representation of the object
        :return: token containing the type and value of the token
        """
        return self.__str__()