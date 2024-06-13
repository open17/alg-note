# 并查集

## 优化
一般路径压缩即可,启发式合并很多时候不利于代码的修改

## 重点
用于维护一种传递关系

## 模板
:::code-group

```py
N=1e5+2
uf=[0]*int(N)
def init(n):
    for i in range(n):
        uf[i]=i
def find(x):
    if uf[x]!=x:
        uf[x]=find(uf[x])
    return uf[x]
def union(x,y):
    uf[find(x)]=find(y)
def check(x,y):
    return find(x)==find(y)
```

:::

## 种类并查集
用于维护维护另一种关系：敌人的敌人是朋友

n个关系维护n个并查集即可
