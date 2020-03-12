"""
    Main enterance of the interpreter
"""
import argparse
from interpreter import Interpreter

def handle_args():
    parser = argparse.ArgumentParser(description='Project to interpret a .c file')
    parser.add_argument('-f', '--file',
            help='.c file to read in and interpret')

    return parser.parse_args()

def main():
    args = handle_args()

    if args.file:
        interpreter = Interpreter()
        exit(interpreter.run(args.file))

if __name__ == '__main__':
    main()