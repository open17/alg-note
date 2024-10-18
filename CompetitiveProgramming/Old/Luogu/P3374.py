import re
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

if "PyPy" in sys.version:
    import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

limits = [100000, 10000, 5000, 2000]
for limit in limits:
    try:
        sys.setrecursionlimit(limit)
        break
    except:
        continue 

def fstream(func):
    def wrapper():
        input_file = open('data.in', 'r')
        sys.stdin = input_file
        output_file = open('data.out', 'w')
        sys.stdout = output_file
        func()
        input_file.close()
        sys.stdin = sys.__stdin__
        output_file.close()
        sys.stdout = sys.__stdout__
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

N=5e5+10
tree=[0]*int(N)

def lowbit(x):
    return x&(-x)

def update(x,val,n):
    while x<=n:
        tree[x]+=val
        x+=lowbit(x)

def query(x):
    res=0
    while x>0:
        res+=tree[x]
        x-=lowbit(x)
    return res

@fstream
# @for_t
def solve():
    n,m=MII()
    a=MII()
    for idx,i in enumerate(a):
        update(idx+1,i,n)
    for i in range(m):
        p,x,y=MII()
        if p&1:
            update(x,y,n)
        else:
            print(query(y)-query(x-1))

solve()