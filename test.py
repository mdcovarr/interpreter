"""
    Test script used to check example .c files in the example/ directory
"""
import os
import glob

CWD = os.path.dirname(os.path.realpath(__file__))
TEST_DIR  = 'examples'


def get_test_files(test_dir):
    test_files = glob.glob(test_dir, recursive=True)

    return test_files

def handle_tests(file_list):
    for filename in file_list:
        c_output = run_c_program(filename)
        my_output = run_interpreter(filename)


def main():
    """
        Main execution begins here.
    """
    # need to get all test files
    test_files = get_test_files(os.path.join(CWD, TEST_DIR, '*'))

    print(test_files)

if __name__ == '__main__':
    main()
