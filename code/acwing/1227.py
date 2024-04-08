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

c=[]


l=1
r=1

for _ in range(n):
    h,w=MII()
    tmp=min(h,w)
    r=max(tmp,r)
    c.append((h,w))
r+=1


def check(a,out=False):
    cnt=0
    for h,w in c:
        if a>h or a>w:
            continue
        cnt+=(h//a)*(w//a)
        if out:
            print(cnt,h,w)
    return cnt>=k

while l<r:
    mid=l+r>>1
    if check(mid):
        l=mid+1
    else:
        r=mid
# print(check(6,True))
print(r-1)