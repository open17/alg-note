# 01字典树

## 什么是?
用于解决一些异或问题,也可以用于模拟平衡树(但是我不会)

## 策略
如果我们要找与给定数异或最大的数，就尽可能走与该数当前位不同的路径
反之则尽可能走与当前位相同的路径

::: tip python提示
在python我们通常用数组模拟,python开定长反而可能耗时大
:::
## 模板

:::code-group

```py
MAXBIT = 31

nxt = [[0,0]]
num = {}
global cnt
cnt=1
def insert(n):
    global cnt
    cur = 1
    for i in range(MAXBIT, -1, -1):
        bit = (n >> i) & 1
        while cur+1>=len(nxt):
            nxt.append([0,0])
        if not nxt[cur][bit]:
            cnt += 1
            nxt[cur][bit] = cnt
        cur = nxt[cur][bit]
    num[cur] = n
def find_max(x):
    cur = 1
    for i in range(MAXBIT, -1, -1):
        bit = (x >> i) & 1
        if nxt[cur][bit ^ 1]:
            cur = nxt[cur][bit ^ 1]
        else:
            cur = nxt[cur][bit]
    return x ^ num[cur]
```

:::