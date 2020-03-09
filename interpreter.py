from pycparser import parse_file, c_parser, c_generator, c_ast

class Interpreter(c_ast.NodeVisitor):
    def __init__(self):
        self.scopes = None

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        return getattr(self, method, self.generic_visit)(node)

    def visit_ID(self, node):
        node.show()

    def visit_Constant(self, node):
        node.show()

    def visit_FileAST(self, node):
        for ext in node.ext:
            if isinstance(ext, c_ast.FuncDef):
                self.visit(ext)

    def visit_FuncDef(self, node):
        print('Yay')
        node.show()

    def visit_Decl(self, node):
        node.show()

    def visit_DeclList(self, node):
        node.show()

    def visit_FuncDecl(self, node):
        node.show()

    def visit_ParamList(self, node):
        node.show()

    def visit_Compound(self, node):
        node.show()

    def visit_Assignment(self, node):
        node.show()

    def visit_If(self, node):
        node.show()

    def visit_BinaryOp(self, node):
        node.show()

    def visit_While(self, node):
        node.show()

    def visit_Return(self, node):
        node.show()

    def read_file(self, filename):
        ast = parse_file(filename, use_cpp=True)
        return ast

    def interpret(self, ast):
        self.visit(ast)
        return 0

    def run(self, filename):
        try:
            ast = self.read_file(filename)
            status = self.interpret(ast)
            return status
        except Exception as e:
            print('Error: {0}'.format(e))
