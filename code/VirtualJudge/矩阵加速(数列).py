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

# 可能会导致pypy产生TLE
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

def matrix_multiply(A, B,mod):
    rows_A,cols_A,cols_B=len(A),len(A[0]),len(B[0])
    res=[[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                res[i][j]+=(A[i][k]*B[k][j])%mod
                res[i][j]%=mod
    return res

def matrix_power(matrix, n,mod=int(1e9+7)):
    rows, cols=len(matrix), len(matrix[0])
    result=[[1 if i==j else 0 for j in range(cols)] for i in range(rows)]
    while n:
        if n%2:
            result=matrix_multiply(result, matrix,mod)
        matrix=matrix_multiply(matrix, matrix,mod)
        n//=2
    return result


@fstream
@for_t
def solve():
    """
    ax-1+ax-3       1 0 1            ax-1  
    ax-1       =    1 0 0      *     ax-2
    ax-2            0 1 0            ax-3
    """
    n=II()
    if n<=3:
        print(1)
    else:
        m=[[1, 0, 1], [1, 0, 0], [0, 1, 0]]
        res=matrix_power(m,n-1)
        print(res[0][0])
solve()