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




def spfa(graph, src):
    """
    src: 源节点
    graph: 邻接表形式的图
    """
    V = len(graph)
    dist = [float("Inf")] * V
    dist[src] = 0

    queue = deque()
    queue.append(src)
    in_queue = [False] * V
    in_queue[src] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    return dist

@fstream
# @for_t
def solve():
    n,m,s=MII()
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w=MII()
        graph[u].append((v,w))
    dist=spfa(graph,s)
    for i in range(1,n+1):
        if dist[i]==float("Inf"):
            dist[i]=2**31-1
        print(dist[i],end=' ')
    print()
solve()