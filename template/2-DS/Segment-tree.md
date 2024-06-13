# 线段树

> 大部分来自pecco的板子

## 什么是?



##  Lazy线段树

> C++板子源自pecco

:::code-group

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 1e5 + 5;
ll tree[MAXN << 2], mark[MAXN << 2], n, m, A[MAXN];
void push_down(int p, int len)
{
    if (len <= 1) return;
    tree[p << 1] += mark[p] * (len - len / 2);
    mark[p << 1] += mark[p];
    tree[p << 1 | 1] += mark[p] * (len / 2);
    mark[p << 1 | 1] += mark[p];
    mark[p] = 0;
}
void build(int p = 1, int cl = 1, int cr = n)
{
    if (cl == cr) return void(tree[p] = A[cl]);
    int mid = (cl + cr) >> 1;
    build(p << 1, cl, mid);
    build(p << 1 | 1, mid + 1, cr);
    tree[p] = tree[p << 1] + tree[p << 1 | 1];
}
ll query(int l, int r, int p = 1, int cl = 1, int cr = n)
{
    if (cl >= l && cr <= r) return tree[p];
    push_down(p, cr - cl + 1);
    ll mid = (cl + cr) >> 1, ans = 0;
    if (mid >= l) ans += query(l, r, p << 1, cl, mid);
    if (mid < r) ans += query(l, r, p << 1 | 1, mid + 1, cr);
    return ans;
}
void update(int l, int r, int d, int p = 1, int cl = 1, int cr = n)
{
    if (cl >= l && cr <= r) return void(tree[p] += d * (cr - cl + 1), mark[p] += d);
    push_down(p, cr - cl + 1);
    int mid = (cl + cr) >> 1;
    if (mid >= l) update(l, r, d, p << 1, cl, mid);
    if (mid < r) update(l, r, d, p << 1 | 1, mid + 1, cr);
    tree[p] = tree[p << 1] + tree[p << 1 | 1];
}
int main()
{
    ios::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 1; i <= n; ++i)
        cin >> A[i];
    build();
    while (m--)
    {
        int o, l, r, d;
        cin >> o >> l >> r;
        if (o == 1)
            cin >> d, update(l, r, d);
        else
            cout << query(l, r) << '\n';
    }
    return 0;
}
```

```py
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

## 动态开点线段树

```cpp
// MAXV一般能开多大开多大，例如内存限制128M时可以开到八百万左右
#define ls(x) tree[x].ls
#define rs(x) tree[x].rs
#define val(x) tree[x].val
#define mark(x) tree[x].mark
const int MAXV = 8e6;
int L = 1, R = 1e5, cnt = 1;
struct node
{
    ll val, mark;
    int ls, rs;
} tree[MAXV];
void upd(int &p, int x, int len)
{
    if (!p) p = ++cnt;
    val(p) += x * len;
    mark(p) += x;
}
void push_down(int p, int len)
{
    if (len <= 1) return;
    upd(ls(p), mark(p), len - len / 2);
    upd(rs(p), mark(p), len / 2);
    mark(p) = 0;
}
ll query(int l, int r, int p = 1, int cl = L, int cr = R)
{
    if (cl >= l && cr <= r) return val(p);
    push_down(p, cr - cl + 1);
    ll mid = (cl + cr - 1) / 2, ans = 0;
    if (mid >= l) ans += query(l, r, ls(p), cl, mid);
    if (mid < r) ans += query(l, r, rs(p), mid + 1, cr);
    return ans;
}
void update(int l, int r, int d, int p = 1, int cl = L, int cr = R)
{
    if (cl >= l && cr <= r) return (void)(val(p) += d * (cr - cl + 1), mark(p) += d);
    push_down(p, cr - cl + 1);
    int mid = (cl + cr - 1) / 2;
    if (mid >= l) update(l, r, d, ls(p), cl, mid);
    if (mid < r) update(l, r, d, rs(p), mid + 1, cr);
    val(p) = val(ls(p)) + val(rs(p));
}
```

## 权值线段树

维护频数数组的线段树

我们可以用它来模拟平衡树

```cpp
void insert(int v) // 插入
{
    update(v, 1);
}
void remove(int v) // 删除
{
    update(v, -1);
}
int countl(int v)
{
    return query(L, v - 1);
}
int countg(int v)
{
    return query(v + 1, R);
}
int rank(int v) // 求排名
{
    return countl(v) + 1;
}
int kth(int k, int p = 1, int cl = L, int cr = R) // 求指定排名的数
{
    if (cl == cr)
        return cl;
    int mid = (cl + cr - 1) / 2;
    if (val(ls(p)) >= k)
        return kth(k, ls(p), cl, mid); // 往左搜
    else
        return kth(k - val(ls(p)), rs(p), mid + 1, cr); // 往右搜
}
int pre(int v) // 求前驱
{
    int r = countl(v);
    return kth(r);
}
int suc(int v) // 求后继
{
    int r = val(1) - countg(v) + 1;
    return kth(r);
}
```

