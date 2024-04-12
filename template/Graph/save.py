n=100

g=[[] for _ in range(n)]


for i in range(n):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)
