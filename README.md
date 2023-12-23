# Python-for-CP
## 简介
个人的算法竞赛python模板,可能不会包含太过于基础的内容(栈,队列,链表等的实现)  

如果没有特殊说明,默认版本`3.8`,编译器`cpython`(一般来说`pypy`也基本检验过)

## 模板目录
### count
> 计数相关的数据结构与算法

- [x]  离散化
- [x]  前缀和与差分
  - [x]  一维前缀和与差分
  - [x]  二维前缀和与差分
- [ ] 二分
  - [ ] 整数二分
  - [ ] 浮点二分
  - [ ] 二分答案
- [ ] 倍增  
- [x] 双指针
  - [x] 相向双指针
  - [x] 滑动窗口 
- [x] 树状数组
- [x] 01Tire
- [ ] 二叉堆
- [x] 平衡树
  - [x] AVL
  - [x] sqlite3模拟(B树) 
  - [ ] 01Tire
  - [ ] Treap
- [ ] 单调栈
- [ ] 单调队列
- [ ] 分块
- [ ] 莫队
### graph
> 图论
- [ ] 搜索
  - [ ] DFS
  - [ ] BFS
  - [ ] 双向BFS
  - [ ] 迭代加深
- [x] 最短路
  - [x] 多源最短路
    - [x] floyd 
  - [x] 单源最短路
    - [x]  dijkstra
    - [x]  bellman-ford
    - [x]  spfa
    - [ ]  01bfs
- [ ] 最小生成树
  - [ ] Kruskal
  - [ ] Prim 
- [x]  并查集
  - [x]  按秩合并&路径压缩并查集
  - [ ]  边权并查集
- [x]  拓扑排序
- [ ] 二分图
  - [ ] 二分图判定
  - [ ] 二分图最大匹配
### math
> 数学
- [x]  数论
  - [x] 欧几里得  
  - [x]  扩展欧几里得
  - [ ]  线性同余方程
  - [ ]  费马小定理
  - [ ]  逆元
  - [ ]  原根
  - [ ]  欧拉函数
  - [x]  数论分块
  - [ ]  素数筛
  - [ ]  质因数分解
  - [ ]  积性函数与筛法
  - [ ]  莫比乌斯反演
  - [ ]  中国剩余定理
- [x]  位运算
  - [x] 位运算与集合论 
  - [ ] 位运算常见性质 
- [ ] 线性代数
  - [ ] 线性基
  - [ ] 高斯消元
- [ ] 概率论
  - [ ] 全概率
  - [ ] 贝叶斯 
  - [ ] 马尔科夫链与随机游走 
- [ ] 计算几何
  - [ ] 凸包
  - [ ] 最近点对 
- [ ] 博弈论
  - [ ] 巴什博弈
  - [ ] 对称博弈
  - [ ] Nim博弈
  - [ ] SG函数 
### string
> 字符串
- [x]  字典树
- [ ]  后缀树
- [ ]  后缀数组
- [ ]  KMP
- [ ]  Z函数
- [ ]  马拉车
- [ ]  字符串哈希

### dp
- [ ] 背包
    - [ ] 0-1 背包
    - [ ] 完全背包
    - [ ] 多重背包
      - [ ] 二进制优化
      - [ ] 单调队列优化
      - [ ] 同余前缀和优化（求方案数）
    - [ ] 分组背包
    - [ ] 树上背包（依赖背包）
    - [ ] 字典序最小方案
- [ ] 线性 DP
  - [ ] 最大子段和
  - [ ] LCS
  - [ ] LPS
  - [ ] LIS
    - [ ] 狄尔沃斯定理
  - [ ] LCIS
  - [ ] 长度为 m 的 LIS 个数
  - [ ] 本质不同子序列个数
- [ ] 区间 DP
- [ ] 环形 DP
- [ ] 博弈 DP
- [ ] 概率 DP
- [ ] 期望 DP
- [ ] 状压 DP
  - [ ] 全排列 DP
  - [ ] 旅行商问题（TSP）
  - [ ] 子集 DP
  - [ ] 高维前缀和（SOS DP）
  - [ ] 插头 DP
- [ ] 数位 DP
  - [ ] 记忆化搜索（同时跑上下界）
- [ ] 倍增优化 DP
- [ ] 斜率优化 DP（CHT）
- [ ] WQS 二分优化 DP（凸优化 DP / 带权二分）
- [ ] 树形 DP
  - [ ] 树的直径个数
  - [ ] 在任一直径上的节点个数
  - [ ] 树上最大独立集
  - [ ] 树上最小顶点覆盖
  - [ ] 树上最小支配集
  - [ ] 树上最大匹配
  - [ ] 换根 DP（二次扫描法）
### others
> 一些其他的内容
- [x]  卡常
- [x]  输入输出







## 输入输出
### 快速框架
```py
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
```
### 标准框架
```py
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

@fstream
@for_t
def solve():
    pass

solve()
```
### 快读
:::warning 貌似有一些问题
:::
```py
def read():
    x = 0
    f = 1
    ch = sys.stdin.buffer.read(1).decode()
    while ch < '0' or ch > '9':
        if ch == '-':
            f = -1
        ch = sys.stdin.buffer.read(1).decode()
    while ch >= '0' and ch <= '9':
        x = x * 10 + int(ch)
        ch = sys.stdin.buffer.read(1).decode()
    return x * f
```
## 语法糖
### zip
下面两个是等价的
```py
c=list(zip(a,b))

c=[(a[i],b[i]) for i in range(min(len(a),len(b)))]
```
注意python3中zip返回的是迭代器,如果需要转为数组请用list
### enumerate
获取下标和值
```py
a=[5,2,0]
for idx,i in enumerate(a):
    print(idx,i)
# 输出
# 0 5
# 1 2
# 2 0
```
### cache
@cache,为函数参数与返回值建立缓存,避免重复计算
通常用于记忆化
### 海象运算符
`(a:=b)`先赋值,再判断
即先给a赋值b,然后外面判断a的性质
比如下面两个是等价的
```py
a=5
if a>4:
    print(a)

if (a:=5)>4:
    print(a)
```
### reduce
返回函数计算的结果
```py
reduce(function, iterable[, initial])
```
### `__slot__`
在python中,类支持动态加载属性,这个时候会开一个哈希,耗时较多
但通常ACM中数据结构不需要动态加载属性,所以可以使用__slot__来限制类只能加载__slot__中定义的属性,从而提高运行速度
```py
self.__slot__ = ['a', 'b']
```
### permutations 与 combinations
k表示选几个,a为数组
`combinations(a: list,k: int)`: 组合,返回迭代器
`permutations(a: list,k: int)`: 排列,返回迭代器
### defaultdict
`defaultdict(type)`,有默认值的字典
### Counter
`Counter(a)`,统计元素个数,类似哈希表的用法
### lambda
匿名函数,常见于`sorted`,`reduce`等
格式:`lambda x:...`,`lambda x,y:...`
### for else
```py
for `临时变量` in `序列`:
    `重复执行的代码`
    ......
else:
    `循环中途没有break正常结束时执行的代码`
```
### 推导式
`[x for x in a]`: 列表推导式
## 常见问题
### 深拷贝
python中对于可变对象一般都是浅拷贝(复制指针)
很多时候对数组我们需要深拷贝,通常方法如下
- `deepcopy(a)`
- `a[::]`
### 字典序
python的str可以直接比较字典序
### 高精度
在python中浮点数的精度是有限的!!![^1]
我们可以通过decimal设置精度限制来实现浮点高精
注意高精度数用字符串传入`Decimal('6.0000003')`
```py
from decimal import Decimal, getcontext
getcontext().prec = 20
```
### 负数取余
python负数取余为正数,无需处理


[^1]: 2023CCPC哈尔滨站血痛的教训
