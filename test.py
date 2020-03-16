"""
    Test script used to check example .c files in the example/ directory
"""
import os
import glob
from subprocess import check_call, check_output
import subprocess

CWD = os.path.dirname(os.path.realpath(__file__))
TEST_DIR  = 'examples'


def get_test_files(test_dir):
    test_files = glob.glob(test_dir, recursive=True)

    return test_files

def run_c_program(filename):
    outfile = './testfile'

    try:
        check_call(['gcc', filename, '-o', outfile])
        status = check_call(outfile, shell=True)
    except subprocess.CalledProcessError as e:
        check_call(['rm', '-rf', outfile])
        return e.returncode

    return status

def run_interpreter(filename):
    try:
        check_call(['python3', '__main__.py', '-f', filename])
    except subprocess.CalledProcessError as e:
        return e.returncode

def check_test(out, my_out):
    if (out == my_out):
        return True
    return False

def print_red(status):
    return "\033[91m {}\033[00m".format(status)

def print_green(status):
    return "\033[92m {}\033[00m".format(status)

def handle_tests(file_list):
    print('\n\n ------------ [ Running Tests ] ------------\n\n')
    i = 0

    for filename in file_list:
        c_output = run_c_program(filename)
        my_output = run_interpreter(filename)

        filename = os.path.basename(filename)
        status = check_test(c_output, my_output)

        if status:
            exit_status = print_green('[pass]')
        else:
            exit_status = print_red('[fail]')

        print('{0}: {1}\t{2}'.format(i, filename, exit_status))

        i += 1


def main():
    """
        Main execution begins here.
    """
    # need to get all test files
    test_files = get_test_files(os.path.join(CWD, TEST_DIR, '*'))

    handle_tests(test_files)

if __name__ == '__main__':
    main()
