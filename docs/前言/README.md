# 旅途的开始
## 第一站-模板
模板中开启本地测试需要传入`--open17`
```R
python template.py --open17
```
```py
import re,os
from io import BytesIO, IOBase
import random
import sys
from math import ceil,floor,fmod,gcd,sqrt,inf
from bisect import bisect_left
from collections import defaultdict,Counter,deque,OrderedDict
from functools import cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy
from typing import *
from string import ascii_lowercase, ascii_uppercase
# 快读区块大小
BUFSIZE = 4096
# 判断是否本地
LOCAL="--open17" in sys.argv

# 可能会导致pypy产生TLE
# if "PyPy" in sys.version:
#     import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

# 调试递归极限
limits = [100000, 10000, 5000, 2000]
for limit in limits:
    try:
        sys.setrecursionlimit(limit)
        break
    except:
        continue 


class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 

def fstream(func):
    def wrapper(is_local):
        input_file = open('data.in', 'r', encoding='utf-8') if is_local else sys.stdin
        output_file = open('data.out', 'w', encoding='utf-8') if is_local else sys.stdout
        sys.stdin = IOWrapper(input_file)
        sys.stdout = output_file
        func()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        if is_local:
            input_file.close()
            output_file.close()
    return wrapper

input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()
 
def II():
    return int(input())
 
def MII():
    return map(int, input().split())
 
def LI():
    return list(input().split())
 
def LII():
    return list(map(int, input().split()))

def for_t(func):
    def wrapper():
        T=II()
        for _ in range(T):
            func()
    return wrapper


@fstream
# @for_t
def solve():
    pass


solve(LOCAL)
```
## 第二站-问题
### 除法
在python中`/`是浮点除法,整除是`//`
### 深拷贝
python中对于可变对象一般都是浅拷贝(复制指针)
很多时候对数组我们需要深拷贝,通常方法如下
- `deepcopy(a)`
- `a[::]`
### 字典序
python的str可以直接比较字典序
### 浮点高精度
在python中浮点数的精度是有限的
我们可以通过导入decimal库来实现浮点高精,其中高精度数用字符串传入
```py
from decimal import Decimal, getcontext
# 精度范围
getcontext().prec = 20
a=Decimal('6.0000003')
```
### 负数取余
python负数取余为正数,无需处理