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

n=II()
a=LII()
l=r=0
p=abs(a[0])

# 头朝左 1   头朝右 0
f=int(a[0]<0)
for v in a:
    # 左边向右
    if abs(v)<p and v>=0:
        l+=1
    # 右边向左
    if abs(v)>p and v<0:
        r+=1
ans=1
if not ((f and l==0) or (not f and r==0)):
    ans+=l+r
print(ans)