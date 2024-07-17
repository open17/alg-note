# 线段树


## 什么是?

可以实现较快的区间修改和区间查询的数据结构

为此我们需要寻找一些特殊的区间,并更新区间的信息

为了避免每次更新退化到 $O(n)$ ,我们可以使用lazy标记优化区间更新过程,这样可以达到 $O(logn)$

证明的话可以从LCA角度然后缩点思考


##  Lazy

下面是一个很基本的模板

其中我喜欢把标记数组记作`todo`

其中`_do`用于处理标记,`_down`用于下传标记,`_up`用于维护树的信息上传

一般只需要修改这三个函数以及查询函数即可

另外一般我们会对有todo的区间节点依然加上todo影响的值,这样查询的时候就不用额外处理下标

:::code-group

```cpp
int val[N];
int node[N << 2], todo[N << 2];

void _do(int p, int size, int v)
{
    node[p] += v * size;
    todo[p] += v;
}

void _down(int p, int l, int r)
{
    if (l >= r)
        return;
    int size = r - l + 1;
    _do(p * 2, size - size / 2, todo[p]);
    _do(p * 2 + 1, size / 2, todo[p]);
    todo[p] = 0;
}

void _up(int p)
{
    node[p] = node[p * 2] + node[p * 2 + 1];
}

void build(int p, int l, int r)
{
    if (l == r)
    {
        node[p] = val[l];
        return;
    }
    int mid = (l + r) >> 1;
    build(p * 2, l, mid);
    build(p * 2 + 1, mid + 1, r);
    _up(p);
}

void update(int p, int l, int r, int L, int R, int v)
{
    if (L <= l and r <= R)
    {
        _do(p, r - l + 1, v);
        return;
    }
    int mid = (l + r) >> 1;
    _down(p, l, r);
    if (mid >= L)
        update(p * 2, l, mid, L, R, v);
    if (mid < R)
        update(p * 2 + 1, mid + 1, r, L, R, v);
    _up(p);
}

i64 query(int p, int l, int r, int L, int R)
{
    if (L <= l and r <= R)
    {
        return node[p];
    }
    _down(p, l, r);
    i64 ans = 0;
    int mid = (l + r) >> 1;
    if (mid >= L)
        ans += query(p * 2, l, mid, L, R);
    if (mid < R)
        ans += query(p * 2 + 1, mid + 1, r, L, R);
    return ans;
}
```

```py
# 我早期的线段树码风,可能和现在的cpp版本不一致
from math import ceil
MAXN=10**5+5
tree=[0 for _ in range(MAXN<<2)]
mark=[0 for _ in range(MAXN<<2)]
a=[0]*MAXN
n=10
def push_down(p,size):
    if size<=1: return 
    tree[p<<1]+=mark[p]*ceil(size/2)
    mark[p<<1]+=mark[p]
    tree[p<<1|1]+=mark[p]*(size//2)
    mark[p<<1|1]+=mark[p]
    mark[p]=0
def build(p=1,cl=1,cr=n):
    if cl==cr:
        tree[p]=a[cl]
        return
    mid=(cl+cr)>>1
    build(p<<1,cl,mid)
    build(p<<1|1,mid+1,cr)
    tree[p]=tree[p<<1]+tree[p<<1|1]
def query(l,r,p=1,cl=1,cr=n):
    if cl >= l and cr <= r: return tree[p]
    push_down(p,cr-cl+1)
    mid=(cl+cr)>>1
    ans=0
    if l <= mid: ans+=query(l,r,p<<1,cl,mid)
    if r > mid: ans+=query(l,r,p<<1|1,mid+1,cr)
    return ans
def update(l,r,val,p=1,cl=1,cr=n):
    if cl >= l and cr <= r:
        tree[p]+=val*(cr-cl+1)
        mark[p]+=val
        return
    push_down(p,cr-cl+1)
    mid=(cl+cr)>>1
    if l <= mid: update(l,r,val,p<<1,cl,mid)
    if r > mid: update(l,r,val,p<<1|1,mid+1,cr)
    tree[p]=tree[p<<1]+tree[p<<1|1]
```

:::
