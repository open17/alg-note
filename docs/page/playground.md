---
lastUpdated: false
---

# :playground_slide: 练习场

支持在线运行python代码,基于[vitepress-python-editor](https://github.com/zqianem/vitepress-python-editor)

## 编辑器
```python:line-numbers
import re,os,random,sys
from math import ceil,floor,fmod,gcd,sqrt,inf
from bisect import bisect_left
from collections import defaultdict,Counter,deque,OrderedDict
from functools import cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip("\r\n")
def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LI(): return list(input().split())
def LII(): return list(map(int, input().split()))
def for_t(func):
    def wrapper():
        for _ in range(II()): func()
    return wrapper
    
# @for_t
def solve():
    a=II()
    print(a)
    
solve()
```
<Editor id="play-ground" max-height="10000px"/>