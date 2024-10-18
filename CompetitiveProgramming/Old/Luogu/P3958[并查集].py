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
N=int(1e5+2)
a=[0]*N
def init(n):
    for i in range(n):
        a[i]=i
def find(x):
    if a[x]!=x:
        a[x]=find(a[x])
    return a[x]
def union(x,y):
    a[find(x)]=find(y)
def check(x,y):
    return find(x)==find(y)

def f(a,b,r):
    ans=0
    for i,j in zip(a,b):
        ans+=(i-j)**2
    return sqrt(ans)<=r*2

@fstream
@for_t
def solve():
    n,h,r=MII()
    init(n+2)
    c=[]
    for i in range(n):
        x,y,z=MII()
        c.append((x,y,z))
        if z-r<=0:
            union(i,n)
        if z+r>=h:
            union(i,n+1)
    if check(n+1,n):
        print('Yes')
        return
    else:
        for i in range(n):
            for j in range(i+1,n):
                if f(c[i],c[j],r):
                    union(i,j)
    if check(n+1,n):
        print('Yes')
    else:
        print('No')

solve()