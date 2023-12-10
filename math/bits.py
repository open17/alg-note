"""
二进制集合技巧

源自灵神的分享: https://leetcode.cn/circle/discuss/CaOJ45/

我们用二进制表示一个集合,1存在0不存在, 例如:
集合A{0,2,3}即'1101', 可以用数字13表示
集合B{1,2}即'110', 可以用6表示

>>> a=13;b=6;
>>> bin(a)[2:]
'1101'
>>> bin(b)[2:]
'110'

交集

>>> a&b
4
>>> bin(a&b)[2:]
'100'

并集

>>> a|b
15
>>> bin(a|v)[2:]
'1111'

差集

>>> a&~b
...

全集{0,1,...,n}

>>> n=5
>>> (1<<(n+1))-1
...

属于
>>> (s >> i) & 1

添加
>>> s | (1 << i)

删除
>>> s&~(1 << i)

删除最小元素(lowbit)
>>> s&(s-1)

元素个数
>>> s.bit_count()

二进制长度
>>> s.bit_length()

集合中的最小元素
>>> (s&-s).bit_length()-1

遍历集合
for i in range(n):
    if (s >> i) & 1:
        pass
        
枚举[0,n-1]全部集合
for s in range(1 << n):
    pass
    
枚举s的非空子集
sub = s
while sub:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s

从大到小枚举 s 的所有子集(s到空)
sub = s
while True:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s
    if sub == s:
        break
"""


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()