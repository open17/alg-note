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


def discrete(a):
    a.sort()
    x = [a[i] for i in range(len(a)) if a[i] != a[i - 1]]
    return x


def check_discrete(b,v):
    return bisect_left(b,v)

@fstream
# @for_t
def solve():
    n=II()
    a=[0,inf,-inf]
    op1=[]
    op2=[]
    op3=[]
    for _ in range(n):
        p=LII()
        if p[0]==1:
            l,r,w=p[1],p[2],p[3]
            op1.append([l,r,w])
            a.extend([l-1,l,r,r+1])
        elif p[0]==2:
            aa,w=p[1],p[2]
            op2.append([aa,w])
            a.extend([aa-1,aa,aa+1])
        else:
            aa,w=p[1],p[2]
            op3.append([aa,w])
            a.extend([aa-1,aa,aa+1])
    b=discrete(a)
    print(b)
    c=[0 for _ in range(len(b))]
    for l,r,w in op1:
        c[check_discrete(b,l)]^=w
        c[check_discrete(b,r+1)]^=w
    for aa,w in op2:
        tmp=check_discrete(b,aa)
        c[tmp]^=w
        c[tmp+1]^=w
    for aa,w in op3:
        tmp=check_discrete(b,aa)
        c[0]^=w
        c[tmp]^=w
        c[tmp+1]^=w
        c[-1]^=w
    ans,res=c[0],0
    for i in range(len(c)):
        c[i]^=c[i-1]
        if c[i]>ans or (c[i]==ans and abs(b[i])<=abs(b[res])):
            ans=c[i]
            res=i
    print(ans,b[res])

solve(LOCAL)