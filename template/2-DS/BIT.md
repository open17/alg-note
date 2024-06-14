# 树状数组

## 什么是?

树状数组是支持单点修改和区间查询的一种简洁优雅的数据结构 (当然转为维护差分数组的话就反过来了)  

树状数组通常用于维护符合结合律的数据(其实最值维护不好处理)  

两种操作时间复杂度logn

## 模板

:::code-group

```cpp
int lowbit(int x){return x&(-x);}
void add(int i,int v,int n){
    while(i<n){
        tree[i]+=v;
        i+=lowbit(i);
    }
}
int query(int i){
    int ans=0;
    while(i>0){
        ans+=tree[i];
        i-=lowbit(i);
    }
    return ans;
}
```

```py
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
    if x<y: return _query(y) - _query(x-1)
    return _query(x) - _query(y-1)
```

:::