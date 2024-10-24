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


n,r=MII()

N=5003
a=[[0] * N for _ in range(N)]

for _ in range(n):
    x,y,w=MII()
    a[x+1][y+1]+=w

for i in range(1, N):
        for j in range(1, N):
            a[i][j] = a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1]
def get(x1,y1,x2,y2):
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]

ans=0
r=min(r,N-1)
for i in range(N):
    if i+r>=N:
        break
    for j in range(N):
        if j+r>=N:
            break
        ans=max(ans,get(i+1,j+1,i+r,j+r))

print(ans)