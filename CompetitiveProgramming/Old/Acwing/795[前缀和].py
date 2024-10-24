import sys
from math import ceil,floor,fmod,gcd,sqrt,inf
from bisect import bisect_left
from collections import defaultdict,Counter,deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy

limits = [100000, 10000, 5000, 2000]
for limit in limits:
    try:
        sys.setrecursionlimit(limit)
        break
    except:
        continue 

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
    
n,m=MII()
a=LII()
a=[0]+a  # 因为python低版本不支持accumalate的设置初始值参数
b = list(accumulate(a))
for _ in range(m):
    i,j=MII()
    print(b[j]-b[i-1])