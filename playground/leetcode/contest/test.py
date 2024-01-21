from lib.leetcode import *
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        path = defaultdict(dict)
        for i in range(n):
            # 到自身最短路为0
            path[i][i]=0
            if i!=0:
                path[i-1][i]=1
                path[i][i-1]=1
        path[x-1][y-1]=1
        path[y-1][x-1]=1
        dist = {}
        for x in path:
            dist[x] = {}
            dist[x][x] = 0
            hpq = [(0, x)]
            while hpq:
                d, u = heappop(hpq)
                if dist[x][u] == d and u in path:
                    for v in path[u]:
                        if v not in dist[x] or dist[x][v] > dist[x][u] + path[u][v]:
                            dist[x][v] = dist[x][u] + path[u][v]
                            heappush(hpq, (dist[x][v], v))