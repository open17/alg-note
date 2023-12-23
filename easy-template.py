import sys
from collections import defaultdict,Counter,deque,OrderedDict
from functools import cache
from bisect import bisect_left
sys.setrecursionlimit(5000)
def II():
    return int(input())
def MII():
    return map(int, input().split())
def LII():
    return list(map(int, input().split()))