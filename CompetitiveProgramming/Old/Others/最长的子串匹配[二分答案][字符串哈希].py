"""
因为某手速场把子序列看成子串而产生的代码

不过后来我发现我真没怎么写过二分+字符串哈希的题,所以就留着了

大概题意:

给长为n的a和长为m的b,求a的前缀字符串s满足:

- 是b的子串

求s的最长长度

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
# LOCAL=False

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
@for_t
def solve():
    n,m=MII()
    a=input()
    b=input()
    
    random.seed()
    MOD1 = 998244353 + random.randint(0, 10007)
    MOD2 = int(1e9+7) + random.randint(0, 233)
    BASE1 = 33 + random.randint(0, 233)
    BASE2 = 133 + random.randint(0, 53)

    b1 = [1]
    b2 = [1]
    h1 = [0]
    h2 = [0]

    for i in range(n):
        b1.append(b1[i] * BASE1 % MOD1)
        b2.append(b2[i] * BASE2 % MOD2)
        h1.append((h1[i] * BASE1 % MOD1 + ord(a[i]) - ord('a')) % MOD1)
        h2.append((h2[i] * BASE2 % MOD2 + ord(a[i]) - ord('a')) % MOD2)  

    # 从0开始,左闭右闭
    def query(l, r):
        hash1 = (h1[r + 1] - h1[l] * b1[r - l + 1] % MOD1 + MOD1) % MOD1
        hash2 = (h2[r + 1] - h2[l] * b2[r - l + 1] % MOD2 + MOD2) % MOD2
        return hash1, hash2
    
    b12 = [1]
    b22 = [1]
    h12 = [0]
    h22 = [0]

    for i in range(m):
        b12.append(b12[i] * BASE1 % MOD1)
        b22.append(b22[i] * BASE2 % MOD2)
        h12.append((h12[i] * BASE1 % MOD1 + ord(b[i]) - ord('a')) % MOD1)
        h22.append((h22[i] * BASE2 % MOD2 + ord(b[i]) - ord('a')) % MOD2)  

    # 从0开始,左闭右闭
    def query2(l, r):
        hash1 = (h12[r + 1] - h12[l] * b12[r - l + 1] % MOD1 + MOD1) % MOD1
        hash2 = (h22[r + 1] - h22[l] * b22[r - l + 1] % MOD2 + MOD2) % MOD2
        return hash1, hash2
    
    def check(k):
        # print(k)
        if k==0:
            return True
        for r in range(n):
            if r+k-1>=min(n,m):
                break
            # print(k, r,query(0, k - 1), query2(r, r+k-1))
            ans= query(0, k - 1) == query2(r, r+k-1)
            if ans:
                return True
        return False
    
    l=0
    r=min(n,m)+1
    while l<r:
        mid=l+r>>1
        if check(mid):
            l=mid+1
        else:
            r=mid
    print(r-1)
    return 0


solve(LOCAL)