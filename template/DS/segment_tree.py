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