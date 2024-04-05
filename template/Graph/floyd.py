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
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])