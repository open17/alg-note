from lib.leetcode import *
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def f(s):
            dist=[[inf for _ in range(n)] for _ in range(n)]
            for i in range(n):
                # 到自身最短路为0
                dist[i][i]=0
            for u,v,w in roads:
                if s>>u&1 and s>>v&1:
                    dist[u][v]=min(dist[u][v],w)
                    dist[v][u]=min(dist[v][u],w)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            for i in range(n):
                if not (s >> i) & 1: continue
                for j in range(n):
                    if (s >> j) & 1 and dist[i][j]>maxDistance:
                        return 0
            return 1
        return sum(f(i) for i in range(1<<n))
