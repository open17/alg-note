# 二进制集合技巧

:::info 参考来源
[0x3f的分享](https://leetcode.cn/circle/discuss/CaOJ45/)
:::

## 概念

我们可以用二进制表示一个集合,1存在0不存在, 例如:

- 集合A{0,2,3},表示为'1101', 即十进制13
- 集合B{1,2},表示为'110', 即十进制6

由此我们可以把一个集合转为二进制数,从而可以使用二进制操作来处理和加速集合的一些操作


## 基本操作

集合的基本操作如下:

|交集|并集|差集|全集|
|--|--|--|--|
|`a&b`|`a\|b`| `a&~b`|`(1<<(n+1))-1`|


|属于|添加|删除|
|--|--|--|
|`(s >> i) & 1`|`s \| (1 << i)`|`s & ~(1 << i)`|

## 进阶操作

一些常用的trick

- 删除最小元素 `s&(s-1)` (即lowbit)
- 元素个数`s.bit_count()`
- 二进制长度`s.bit_length()`
- 集合中的最小元素`(s&-s).bit_length()-1`

快速获取每一位1的下标

```py
while n:
    idx=int(log2(n&-n))
    n&=(n-1)
    # 或者n-=n&(-n)
```

## 二进制枚举

::: code-group

```py
n=20
s=6

# 遍历集合
for i in range(n):
    if (s >> i) & 1:
        pass
    
# 枚举[0,n-1]全部集合
for s in range(1 << n):
    pass

# 枚举s的非空子集
sub = s
while sub:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s

# 从大到小枚举 s 的所有子集(s到空)
sub = s
while True:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s
    if sub == s:
        break
```

:::
