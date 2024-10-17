"""
对顶堆

这题洛谷题面很有问题
没有保证输入数据按照题目条件的a一行b一行
a和b其实可能有多行
我知道大部分人都是cpp一个个读的,但python正常习惯按行读
按照题目就会RE

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


lo_heap=[]
hi_heap=[]
def insert(x):
    if not lo_heap or x>=lo_heap[0]:
        heappush(lo_heap,x)
    else:
        heappush(hi_heap,-x)
        

def find():
    return lo_heap[0]

def update(k):
    size=len(hi_heap)+len(lo_heap)
    if k>size:
        return
    while len(lo_heap)<k:
        if hi_heap: 
            heappush(lo_heap,-heappop(hi_heap))
        else: 
            break
    while len(hi_heap)<size-k:
        heappush(hi_heap,-heappop(lo_heap))


@fstream
# @for_t
def solve():
    n,m=MII()
    a=LII()
    while len(a)<n:
        a+=LII()
    b=LII()
    while len(b)<m:
        b+=LII()
    # c=[]
    i=1
    pp=0
    for p in b:
        while pp+1<=p and pp<len(a):
            insert(-a[pp])
            # c.append(a[pp])
            # c.sort()
            update(i)
            pp+=1
        print(-find())
        i+=1
        update(i)
        
solve()