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

MAXN=10**5+5
tree=[0 for _ in range(MAXN<<2)]
mark=[0 for _ in range(MAXN<<2)]
a=[0]*MAXN

@fstream
# @for_t
def solve():
    n,m=MII()
    aa=LII()
    for i in range(n):
        a[i+1]=aa[i]
    def push_down(p,size):
        if size<=1: return 
        tree[p<<1]+=mark[p]*ceil(size/2)
        mark[p<<1]+=mark[p]
        tree[p<<1|1]+=mark[p]*(size//2)
        mark[p<<1|1]+=mark[p]
        mark[p]=0
    def build(p=1,cl=1,cr=n):
        if cl==cr:
            tree[p]=a[cl]
            return
        mid=(cl+cr)>>1
        build(p<<1,cl,mid)
        build(p<<1|1,mid+1,cr)
        tree[p]=tree[p<<1]+tree[p<<1|1]
    def query(l,r,p=1,cl=1,cr=n):
        if cl >= l and cr <= r: return tree[p]
        push_down(p,cr-cl+1)
        mid=(cl+cr)>>1
        ans=0
        if l <= mid: ans+=query(l,r,p<<1,cl,mid)
        if r > mid: ans+=query(l,r,p<<1|1,mid+1,cr)
        return ans
    def update(l,r,val,p=1,cl=1,cr=n):
        if cl >= l and cr <= r:
            tree[p]+=val*(cr-cl+1)
            mark[p]+=val
            return
        push_down(p,cr-cl+1)
        mid=(cl+cr)>>1
        if l <= mid: update(l,r,val,p<<1,cl,mid)
        if r > mid: update(l,r,val,p<<1|1,mid+1,cr)
        tree[p]=tree[p<<1]+tree[p<<1|1]
    build()
    for _ in range(m):
        op=LII()
        if op[0]==1:
            update(op[1],op[2],op[3])
        else:
            print(query(op[1],op[2]))
    return 0


solve(LOCAL)