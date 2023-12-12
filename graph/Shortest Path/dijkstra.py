"""
堆优化的dijkstra, O(mlogm)
原理: 贪心操作取距离顶点最近且没有被访问过的点松弛
所以无法处理负权
"""
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