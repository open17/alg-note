# 卡常技巧


## python

### 初始化优化
python中推导式初始化比for循环快


### 插入优化

```py
>>> a=[1,3,4,5]
>>> i=1
>>> v=2
>>> a[i:i]=[v]
```

a[i:i] = [v] 的底层实现,其中i为要插入的位置,v为值:
调用c的memmove 库函数来搬运插入之后的元素,
快于insert


### __slot__优化
python的class一般都比较慢,可以加入__slot__来优化

### array优化

使用array替代list,注意array是定内容类型的,比如指定只能int

### 手写汇编

```py
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
```