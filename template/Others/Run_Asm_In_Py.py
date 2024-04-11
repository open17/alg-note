from ctypes import *

# 汇编代码转换为字节流
def translate_asm(asm_code):
    res = b''
    for line in asm_code.split('\n'):
        if not ':' in line or '>:' in line:
            continue
        line = line[line.find(':')+1:].strip()
        line = line[:line.find('   ')].strip()
        for byte in line.split(' '):
            res += int(byte, 16).to_bytes(1, byteorder='little')
    return res

# 编译汇编代码并返回函数指针
def compile_asm(asm_code, func_type):
    buf = create_string_buffer(translate_asm(asm_code))
    return CFUNCTYPE(func_type)(cast(buf, POINTER(c_void_p)).contents.value)

# 示例：求两个整数之和
asm_code = '''
section .text
global _add_two_numbers

_add_two_numbers:
    mov eax, edi
    add eax, esi
    ret
'''

# 定义函数类型
AddTwoNumbersFunc = CFUNCTYPE(c_int, c_int, c_int)

# 编译汇编代码
add_two_numbers = compile_asm(asm_code, AddTwoNumbersFunc)

# 调用汇编函数
result = add_two_numbers(3, 5)
print("Result:", result)