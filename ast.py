class Node(object):
    def __init__(self, line):
        self.line = line


class Expression(Node):
    def __init__(self, children, line):
        Node.__init__(self, line)
        self.children = children


class Num(Node):
    """
    Node to hold a numerical value
    """
    def __init__(self, token, line):
        """
        Default Constructor
        :param token: Num Token
        :param line:
        """
        Node.__init__(self, line)
        self.token = token
        self.value = token.value


class Var(Node):
    def __init__(self, token, line):
        Node.__init__(self, line)
        self.token = token
        self.value = token.value


class String(Node):
    def __init__(self, token, line):
        Node.__init__(self, line)
        self.token = token
        self.value = token.value


class Assign(Node):
    def __init__(self, var, op, exp, line):
        Node.__init__(self, line)
        self.left = var
        self.right = exp
        self.op = op
        self.token = op


class IfStatement(Node):
    def __init__(self, boolean_expr, true_block, line, false_block=None):
        Node.__init__(self, line)
        self.condition = boolean_expr
        self.true_block = true_block
        self.false_block = false_block


class WhileStatement(Node):
    def __init__(self, boolean_expr, block, line):
        Node.__init__(self, line)
        self.condition = boolean_expr
        self.block = block


class ForStatement(Node):
    def __init__(self, initial, boolean_expr, increment, block, line):
        Node.__init__(self, line)
        self.initial = initial
        self.condition = boolean_expr
        self.increment = increment
        self.block = block


class ReturnStatement(Node):
    def __init__(self, expression, line):
        Node.__init__(self, line)
        self.expression = expression


class BinaryOp(Node):
    def __init__(self, s1, op, s2, line):
        Node.__init__(self, line)
        self.left = s1
        self.right = s2
        self.token = op
        self.op = op


class VariableDeclaration(Node):
    def __init__(self, variable_node, type_node, line):
        Node.__init__(self, line)
        self.variable_node = variable_node
        self.type_node = type_node


class CompoundStatements(Node):
    def __init__(self, children, line):
        Node.__init__(self, line)
        self.children = children


class Patameter(Node):
    def __init__(self, var_node, type_node, line):
        Node.__init__(self, line)
        self.var_node = var_node
        self.type_node = type_node


class FunctionDeclaration(Node):
    def __init__(self, type_node, func_name, parameters, block, line):
        Node.__init__(self, line);
        self.type_node = type_node
        self.func_name = func_name
        self.parameters = parameters
        self.block = block


class FunctionBlock(Node):
    def __init__(self, children, line):
        Node.__init__(self, line)
        self.children = children


class Program(Node):
    def __init__(self, statements, line):
        Node.__init__(self, line)
        self.children = statements

