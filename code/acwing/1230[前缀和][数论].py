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


n,k=MII()
# 1 3 6 10 15
a=[0]
d=defaultdict(int)
d[0]=1
ans=0
for i in range(n):
    p=II()
    a.append((a[-1]+p%k)%k)
    ans+=d[a[-1]]
    d[a[-1]]+=1
print(ans)


