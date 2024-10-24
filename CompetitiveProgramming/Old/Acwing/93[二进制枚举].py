import sys
from math import ceil,floor,fmod,gcd,sqrt,inf,log2
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

for i in range((1<<n)-1,(1<<m)-2,-1):
    ans=[]
    while i:
        lowbit=i&(-i)
        ans.append(n-int(log2(lowbit)))
        i-=lowbit
        if len(ans)>m:
            break
    else:
        if len(ans)==m:
            print(*ans[::-1])