from __future__ import print_function
import sys

from pycparser import parse_file, c_parser, c_generator

if __name__ == '__main__':
    if len(sys.argv) > 1:
            ast = parse_file(sys.argv[1], use_cpp=True)
            ast.show()
            generator = c_generator.CGenerator()
            print(generator.visit(ast)) 