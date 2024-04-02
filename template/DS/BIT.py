"""
树状数组是支持单点修改和区间查询的一种简洁优雅的数据结构
(当然转为维护差分数组的话就反过来了)
树状数组通常用于维护符合结合律的数据(其实最值维护不好处理)
两种操作时间复杂度logn

为什么不封装?因为在算法竞赛中通常python的class比较消耗时间(即使__slot__优化)

注意树状数组的下标从1开始

注意update下面是增加x,不是更新为x

>>> update(1,1,3);update(2,2,3);update(3,3,3)
>>> query(1,1)
1
>>> query(1,3)
6
>>> query(2,3)
5
>>> update(2,-2,3)
>>> query(2,3)
3
>>> query(1,2)
1
"""

N=1e5+10
tree=[0]*int(N)

def lowbit(x):
    return x&(-x)

def update(x,val,n):
    while x<=n:
        tree[x]+=val
        x+=lowbit(x)

def _query(x):
    res=0
    while x>0:
        res+=tree[x]
        x-=lowbit(x)
    return res

def query(x,y):
    if x<y:
        return _query(y) - _query(x-1)
    return _query(x) - _query(y-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()