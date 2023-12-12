import subprocess
import sys
def fstream(func):
    def wrapper():
        output_file = open('duipai.out', 'w')
        sys.stdout = output_file
        func('testcase.txt')
        output_file.close()
        sys.stdout = sys.__stdout__
    return wrapper
def run_exe(input_file):
    output = subprocess.check_output(['duipai.exe'], stdin=open(input_file), text=True)
    return output.strip().split('\n')

def run_py(input_file):
    output = subprocess.check_output(['python', 'P3369.py'], stdin=open(input_file), text=True)
    return output.strip().split('\n')

def compare_outputs(exe_output, py_output):
    if len(exe_output) != len(py_output):
        return False

    for i in range(len(exe_output)):
        if exe_output[i] != py_output[i]:
            return False

    return True

@fstream
def test_case(input_file):
    while 1:
        exe_output = run_exe(input_file)
        py_output = run_py(input_file)

        if compare_outputs(exe_output, py_output):
            print("Test case passed,Continue..")
            break
            subprocess.check_output(['python', 'duipai/data.py'], stdin=open(input_file), text=True)
        else:
            print("Test case failed")
            print("a.exe output: ", exe_output)
            print("a.py output: ", py_output)
            break

input_file = 'testcase.txt'
test_case()