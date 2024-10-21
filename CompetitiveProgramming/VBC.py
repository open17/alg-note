import subprocess
import sys

def execute_program(input_file, program, provide_input=True):
    try:
        if program.endswith(".exe"):
            if provide_input:
                output = subprocess.check_output([program], stdin=open(input_file), text=True)
            else:
                output = subprocess.check_output([program], text=True)
        elif program.endswith(".py"):
            if provide_input:
                output = subprocess.check_output(['python', program], stdin=open(input_file), text=True)
            else:
                output = subprocess.check_output(['python', program], text=True)
        else:
            raise ValueError("Unsupported program type. Only .exe and .py are supported.")
        
        return output.strip().split('\n')
    
    except subprocess.CalledProcessError as e:
        print(f"Error running {program}: {e}")
        return []

def compare_outputs(output1, output2):
    if len(output1) != len(output2):
        return False
    return all(line1 == line2 for line1, line2 in zip(output1, output2))

def redirect_stdout_to_file(func):
    def wrapper():
        global RESULT_FILE_NAME
        with open(RESULT_FILE_NAME, 'w') as output_file:
            sys.stdout = output_file
            func()
            sys.stdout = sys.__stdout__
    return wrapper

def run_single_test(input_file, program1, program2):
    program1_output = execute_program(input_file, program1)
    program2_output = execute_program(input_file, program2)

    if compare_outputs(program1_output, program2_output):
        print("AC, Continue..")
        return True
    else:
        print("WA")
        print(f"{program1} output:\n{program1_output}")
        print(f"{program2} output:\n{program2_output}")
        return False

@redirect_stdout_to_file
def test_case_single():
    global TESTCASE_FILE, PROGRAM_1, PROGRAM_2
    print(f"Test File {TESTCASE_FILE}",end=" ")
    run_single_test(TESTCASE_FILE, PROGRAM_1, PROGRAM_2)

@redirect_stdout_to_file
def test_case_auto_generated():
    global DATA_GENERATOR, MAX_TESTS, PROGRAM_1, PROGRAM_2, DATA_GENERATOR_OUTPUT
    for i in range(MAX_TESTS):
        with open(DATA_GENERATOR_OUTPUT,"w") as f:
            for li in execute_program(None, DATA_GENERATOR, provide_input=False):
                f.write(f"{li}\n")
        print(f"Test case # {i+1}",end=" ")
        ans=run_single_test(DATA_GENERATOR_OUTPUT, PROGRAM_1, PROGRAM_2)
        if not ans:
            break

if __name__ == "__main__":

    RESULT_FILE_NAME = "result_output.txt"

    # 单个测试用例
    TESTCASE_FILE = 'output_auto.txt'
    

    # 自动生成测试用例并测试
    DATA_GENERATOR = "data_generator.py"
    DATA_GENERATOR_OUTPUT="output_auto.txt"
    MAX_TESTS = 10000

    PROGRAM_1 = "test/a.exe"
    PROGRAM_2 = "test/sample.exe"
    
    # test_case_single()
    test_case_auto_generated()