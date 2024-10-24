"""
卡常题
"""
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

# if "PyPy" in sys.version:
#     import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

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

N=5003
a=[[0] * N for _ in range(N)]
@fstream
# @for_t
def solve():
    n,m=MII()
    for _ in range(n):
        x,y,v=MII()
        a[x+1][y+1]+=v
    for i in range(1, N):
        for j in range(1, N):
            a[i][j] = a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1]
    def get(x1,y1,x2,y2):
        return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]
    ans=0
    m=min(N-1,m)
    for i in range(m,N):
        for j in range(m,N):
            ans=max(ans,get(i-m+1,j-m+1,i,j))
    print(ans)
solve()