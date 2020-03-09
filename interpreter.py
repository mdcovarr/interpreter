from pycparser import parse_file, c_parser, c_generator, c_ast

class Interpreter(c_ast.NodeVisitor):
    def __init__(self):
        pass

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        return getattr(self, method, self.generic_visit)(node)

    def visit_ID(self, node):
        node.show()

    def visit_Constant(self, node):
        node.show()

    def visit_FileAST(self, node):
        node.show()

    def visit_FuncDef(self, node):
        node.show()

    def visit_Decl(self, node):
        node.show()

    def visit_DeclList(self node):
        node.show()

    def visit_FuncDecl(self, node):
        node.show()

    def visit_ParamList(self, node):
        node.show()

    def visit_Compound(self, node):
        node.show()

    def visit_Assignment(node):
        node.show()

    def visit_If(self, node):
        node.show()

    def visit_BinaryOp(self, node):
        node.show()

    def visit_While(self, node):
        node.show()

    def visit_Return(self, node):
        node.show())

    def read_file(self, filename):
        ast = parse_file(sys.argv[1], use_cpp=True)
        return ast

    def interpret(self, ast):
        self.visit(ast)

    @staticmethod
    def run(filename):
        try:
            reader = Interpreter()
            ast = reader.read_file(filename)
            status = reader.interpret(ast)
        except Exception as e:
            print('Error: {0}'.format(e))