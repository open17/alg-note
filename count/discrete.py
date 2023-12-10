"""
离散化是一种预处理手段,当原数据很大或含有负数、小数时我们会进行离散化

离线离散化: 一般我们通常考虑数据之间的大小关系进行离散化,所以需要离线
在线离散化: 在某些情况我们不关心数据之间的大小,可以在线离散

下面是离线离散化(在线离散化一般哈希就好了)

>>> a=discrete([5,5,3,1,2,3,3,9,1]);print(a)
[1, 2, 3, 5, 9]
>>> check_discrete(a,5)
3
"""
from bisect import bisect_left

def discrete(a):
    a.sort()
    x = [a[i] for i in range(len(a)) if a[i] != a[i - 1]]
    return x

def check_discrete(b,v):
    return bisect_left(b,v)

if __name__ == "__main__":
    import doctest
    doctest.testmod()