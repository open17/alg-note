# 离散化

## 什么是?

离散化是一种预处理手段,当原数据很大或含有负数、小数时我们会进行离散化

一般结合线段树等数据结构使用

## 区别
- 离线离散化: 一般我们通常考虑数据之间的大小关系进行离散化,所以需要离线
- 在线离散化: 在某些情况我们不关心数据之间的大小,可以在线离散

## 模板

下面是离线离散化(在线离散化一般哈希就好了)

:::code-group

```py
from bisect import bisect_left

def discrete(a):
    a.sort()
    x = [a[i] for i in range(len(a)) if a[i] != a[i - 1]]
    return x

def check_discrete(b,v):
    return bisect_left(b,v)
```

:::