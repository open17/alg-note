# 建图

## 邻接矩阵
`g[x][y]` 为0/1/边权,表示是否x有向y的边  


## 邻接表

个人喜欢用这个

```py
n=100

g=[[] for _ in range(n)]


for i in range(n):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)
```

## 链式前向星
本质上是用链表实现的邻接表
