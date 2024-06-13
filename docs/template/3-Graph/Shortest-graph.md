# 最短路

## 堆优化Dijkstra算法
- 时间$O(mlogm)$ 
- 原理: 贪心操作取距离顶点最近且没有被访问过的点松弛
- 所以无法处理负权
:::code-group

```py
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from math import inf

def dijkstra(graph, src):
    n=len(graph)
    dist=[inf]*n
    dist[src]=0
    visited=[0]*n
    heap=[(0,src)]
    while heap:
        d,u=heappop(heap)
        if visited[u]:
            continue
        visited[u]=1
        for v,w in graph[u]:
            dist[v]=min(dist[v],dist[u]+w)
            heappush(heap,(dist[v],v))
    return dist
```

:::

## SPFA
- 队列优化的bellman-ford,去掉无用的松弛操作
- 但依然可能被卡成bellman-ford
- 在网络流中用的比较多
- 判负权环:
    - 用数组记录顶点进队的次数
    - 当一个顶点进队超过n次时,存在负权环
:::code-group

```py
from collections import deque

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
    in_queue = [0] * V
    in_queue[src] = 1

    while queue:
        u = queue.popleft()
        in_queue[u] = 0
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = 1
    return dist
```

:::

## 弗洛伊德
- 允许负权，不允许负环
- 多源最短
- 立方复杂度
:::code-group

```py
from math import inf
N=1e3+5
dist=[[inf for _ in range(N)] for _ in range(N)]

def init(n):
    for i in range(n):
        # 到自身最短路为0
        dist[i][i]=0

def floyd(n):
    for k in range(n):
        for i in range(n):
            # 小trick优化剪枝
            if dist[i][k] == inf: continue
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
```

:::