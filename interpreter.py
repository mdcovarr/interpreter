from pycparser import parse_file, c_parser, c_generator, c_ast
from memory import Memory


class Interpreter(c_ast.NodeVisitor):
    def __init__(self):
        # memory storage for variables
        self.memory = Memory()

    def visit(self, node):
        """
        Function used to call visit functions of different type of
        Nodes in the AST
        """
        method = 'visit_' + node.__class__.__name__
        return getattr(self, method, self.generic_visit)(node)

    def visit_ID(self, node):
        """
        Function used to get a value from memory
        :param node: ID node with name of variable
        :return value: value stored in memory
        """
        value = self.memory[node.name]

        return value

    def visit_Constant(self, node):
        """
        Function used to visit constant value node
        :param node:
        :return: return the value of the constant
        """
        return int(node.value)

    def visit_FileAST(self, node):
        """
        Function used to handle the start of analyzing the AST
        :param node: the root node of the AST
        :return None:
        """
            for ext in node.ext:
                if isinstance(ext, c_ast.FuncDef):
                    self.visit(ext)

    def visit_FuncDef(self, node):
        """
        Function used to handle function definition node
        :param node: function definition node
        :return: result of executing the function body
        """
        decl = node.decl
        # need to add parameters of function to memory

        if node.decl.type.args:
            for i, arg in enumerate(node.decl.type.args.params):
                self.memory[arg.name] = self.memory.stack.current_frame.current_scope.values.pop(i)
        return self.visit(node.body)

    def visit_TypeDecl(self, node):
        """
        Function used for a type declaration
        :param node: Node with declaration variable
        :return None:
        """
        # need to store new type declaration.
        self.memory.declare_variable(node.declname)

    def visit_Decl(self, node):
        """
        Function used to determine how to handle declaration
        :param node: AST Node analyzing
        :return None:
        """
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
        Function used to execute the assign statement in a declaration
        :param node:
        :return None:
        """
        key = node.name
        self.memory[key] = self.visit(node.init)

    def visit_DeclList(self, node):
        """
        Function used to handle list of declarations
        :param node: declaration list node in AST
        :return None:
        """
        for decl in node.decls:
            self.visit(decl)

    def visit_FuncDecl(self, node):
        """
        Function used to handle function definition of a C program
        :param node: function definition in the AST
        :return None:
        """
        param_list = node.args
        self.visit(param_list)

    def visit_ParamList(self, node):
        """
        Function used to handle parameter list
        :param self:
        :param node:
        :return:
        """
        for i, param in enumerate(node.params):
            print ('{0}: {1}'.format(i, param))

    def visit_Compound(self, node):
        """
        Function used to handle compound statements
        :param node: compound node in AST
        :return: return node expression evaluated
        """
        for stmt in node.block_items:
            if isinstance(stmt, c_ast.Return):
                return self.visit(stmt)
            self.visit(stmt)

    def visit_Assignment(self, node):
        """
        Function used to handle assignment statement
        :param node: assignment node
        :return: assignment value
        """
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

        return self.memory[var]

    def visit_If(self, node):
        """
        Function used to handle C language If statements
        :param node: If statement node in AST
        :return None:
        """
        if self.visit(node.cond):
            self.visit(node.iftrue)
        else:
            self.visit(node.iffalse)

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
        """
        Function used to handle While statement
        :param node: node pertaining to while implementation in the AST
        :return None:
        """
        while self.visit(node.cond):
            self.visit(node.stmt)

    def visit_For(self, node):
        """
        Function used to handle the For statement
        :param node:
        :return:
        """
        self.visit(node.init)
        while self.visit(node.cond):
            self.visit(node.stmt)
            self.visit(node.next)

    def visit_Return(self, node):
        """
        Function used to handle the return statement
        :param node: return AST node
        :return: the evaluated return expression
        """
        return self.visit(node.expr)

    def read_file(self, filename):
        """
        Function used to read C program file
        :param self:
        :param filename:
        :return:
        """
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
        """
        Loading function into the GLOBAL scope
        :param node:
        :return None:
        """
        name = node.decl.name
        self.memory[name] = node

    def get_functions(self, ast):
        """
        iterating through all function declarations
        :param ast: AST representation of the read in file
        :return None:
        """
        for ext in ast.ext:
            if isinstance(ext, c_ast.FuncDef):
                self.load_function(ext)

    def run(self, filename):
        try:
            ast = self.read_file(filename)
            status = self.interpret(ast)
            return status
        except Exception as e:
            print('Error Attempting to interpret C program, exiting...')
