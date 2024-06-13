# 前缀和与差分

## 定义
使用O(n)的时间预处理,然后将后续的查询/操作转为O(1)的复杂度

前缀和可以支持O(1)的区间查询

差分支持O(1)的区间修改

## 重点

- 也常用于操作转换(区间转单点,单点转区间)
- 注意差分思想不局限于维护加减,实际上可以维护具备结合律的关系,比如异或关系

## 模板

:::code-group

```py
from itertools import accumulate

"""
一维前缀和
"""
a=[1,5,2,3,2]
b=[0]
for i in a:
    b.append(b[-1]+i)
# 求区间[i,j]
j,i=3,1
print(b[j+1]-b[i])


# 更简洁的写法
b = list(accumulate(a, initial=0))

"""
一维差分
给区间[l, r]中的每个数加上c:
b[l] += c, b[r + 1] -= c
"""

"""
二维前缀和
原地trick
"""
N=5003
a=[[0] * N for _ in range(N)]
for i in range(1, N):
        for j in range(1, N):
            a[i][j] = a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1]
def get(x1,y1,x2,y2):
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]

"""
二维差分
"""
N = 5003
a = [[0] * N for _ in range(N)]

def update(x, y, val):
    a[x][y] += val

def get(x1, y1, x2, y2):
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]
```

:::