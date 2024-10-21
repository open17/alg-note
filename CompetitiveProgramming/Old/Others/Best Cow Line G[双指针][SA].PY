"""
给卡常了
"""
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

def buildSA(s):
    n = len(s)
    x = [0] * n
    y = [0] * n
    sa = [0] * (n + 1)
    rk = [0] * (n + 1)
    m = 200
    for i in range(n):
        x[i] = ord(s[i])
        y[i] = i
    indexSort(m, sa, x, y)
    k = 1
    while k <= n and m != n:
        num = 0
        for i in range(n - k, n):
            y[num] = i
            num += 1
        for i in range(1, n + 1):
            if sa[i] >= k:
                y[num] = sa[i] - k
                num += 1
        indexSort(m, sa, x, y)
        num = 1
        x, y = y, x
        for i in range(1, n + 1):
            y1 = y[sa[i] + k] if sa[i] + k < n else 0
            y2 = y[sa[i - 1] + k] if sa[i - 1] + k < n else 0
            if i != 1 and (y[sa[i]] != y[sa[i - 1]] or y1 != y2):
                num += 1
            x[sa[i]] = num
        k *= 2
        m = num
    for i in range(1, n + 1):
        sa[i]+=1
        rk[sa[i]] = i
    return sa[1:], rk[1:]

def indexSort(m, sa, x, y):
    c = [0] * (m + 1)
    n = len(x)
    for i in range(n):
        c[x[y[i]]] += 1
    for i in range(1, m + 1):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        sa[c[x[y[i]]]] = y[i]
        c[x[y[i]]] -= 1

@fstream
def solve():
    a=""
    flag=1
    @for_t
    def init():
        nonlocal a,flag
        a+=I()
        if flag and a[0]!=a[-1]:
            flag=0
    init()
    """
    a b c c b a
    r=2 4  2n+1-r
    """
    sa,rk=buildSA(a+'0'+a[::-1])
    l,r=0,len(a)-1
    cnt=0
    while l<=r:
        if a[l]<a[r] or (a[l]==a[r] and rk[l]<=rk[2*len(a)-r]):
            ans=a[l]
            l+=1
        else:
            ans=a[r]
            r-=1
        print(ans,end='')
        cnt+=1
        if cnt==80:
            print()
            cnt=0
solve(LOCAL)