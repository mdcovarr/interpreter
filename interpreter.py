from pycparser import parse_file, c_parser, c_generator, c_ast
from memory import Memory


class Interpreter(c_ast.NodeVisitor):
    def __init__(self):
        self.memory = Memory()

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        return getattr(self, method, self.generic_visit)(node)

    def visit_ID(self, node):
        # need to get value from scope
        value = self.memory[node.name]

    def visit_Constant(self, node):
        return int(node.value)

    def visit_FileAST(self, node):
            for ext in node.ext:
                if isinstance(ext, c_ast.FuncDef):
                    self.visit(ext)

    def visit_FuncDef(self, node):
        decl = node.decl
        # need to add parameters of function to memory
        if node.decl.type.args:
            for i, arg in enumerate(node.decl.type.args.params):
                self.memory[arg.name] = self.memory.stack.current_frame.current_scope.values.pop(i)
        return self.visit(node.body)

    def visit_TypeDecl(self, node):
        """
        Function used for a type declaration
        :param node:
        :return:
        """
        # need to store new type declaration.
        self.memory.declare_variable(node.declname)

    def visit_Decl(self, node):
        # node.name = the name of the function
        # need to catch the different type of declarations
        if isinstance(node.type, c_ast.TypeDecl):
            self.visit(node.type)
            self.visit_Assign(node)
        elif isinstance(node.type, c_ast.FuncDecl):
            func_decl = node.type
            self.visit(func_decl)

    def visit_Assign(self, node):
        """
        Function used to execute the assign statement
        :param node:
        :return:
        """
        key = node.name
        self.memory[key] = self.visit(node.init)

    def visit_DeclList(self, node):
        node.show()

    def visit_FuncDecl(self, node):
        param_list = node.args
        self.visit(param_list)

    def visit_ParamList(self, node):
        for i, param in enumerate(node.params):
            print ('{0}: {1}'.format(i, param))

    def visit_Compound(self, node):
        for stmt in node.block_items:
            if isinstance(stmt, c_ast.Return):
                return self.visit(stmt)
            self.visit(stmt)

    def visit_Assignment(self, node):
        var = node.lvalue.name
        op = node.op

        if op == '=':
            self.memory[var] = self.visit(node.rvalue)
        elif op == '+=':
            self.memory[var] += self.visit(node.rvalue)
        elif op == '-=':
            self.memory[var] -= self.visit(node.rvalue)
        elif op == '/=':
            self.memory[var] /= self.visit(node.rvalue)
        elif op == '*=':
            self.memory[var] *= self.visit(node.rvalue)


    def visit_If(self, node):
        node.show()

    def visit_BinaryOp(self, node):
        """
        Function used to determine return from binary operator
        :param node: binary operator node
        :return: Evaluated binary operation
        """
        op = node.op

        if op == '+':
            return self.visit(node.left) + self.visit(node.right)
        elif op == '-':
            return self.visit(node.left) - self.visit(node.right)
        elif op == '/':
            return self.visit(node.left) / self.visit(node.right)
        elif op == '*':
            return self.visit(node.left) * self.visit(node.right)
        elif op == '%':
            return self.visit(node.left) % self.visit(node.right)
        elif op == '*':
            return self.visit(node.left) * self.visit(node.right)
        elif op == '<':
            return self.visit(node.left) < self.visit(node.right)
        elif op == '>':
            return self.visit(node.left) > self.visit(node.right)
        elif op == '>=':
            return self.visit(node.left) >= self.visit(node.right)
        elif op == '<=':
            return self.visit(node.left) <= self.visit(node.right)
        elif op == '&&':
            return self.visit(node.left) and self.visit(node.right)
        elif op == '||':
            return self.visit(node.left) or self.visit(node.right)
        elif op == '==':
            return self.visit(node.left) == self.visit(node.right)
        elif op == '!=':
            return self.visit(node.left) != self.visit(node.right)

    def visit_While(self, node):
        node.show()

    def visit_Return(self, node):
        return self.visit(node.expr)

    def read_file(self, filename):
        ast = parse_file(filename, use_cpp=True)
        return ast

    def create_main_frame(self):
        """
        Function used to create the main frame
        :return None:
        """
        self.memory.add_frame('main')

    def interpret(self, ast):
        self.get_functions(ast)
        self.create_main_frame()
        exit_status = self.visit(self.memory['main'])

        return exit_status

    def load_function(self, node):
        name = node.decl.name
        self.memory[name] = node

    def get_functions(self, ast):
        for ext in ast.ext:
            if isinstance(ext, c_ast.FuncDef):
                self.load_function(ext)

    def run(self, filename):
        try:
            ast = self.read_file(filename)
            status = self.interpret(ast)
            return status
        except Exception as e:
            print('Error: {0}'.format(e))
