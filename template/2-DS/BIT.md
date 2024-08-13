# 树状数组

## 什么是?

树状数组是支持单点修改和区间查询的一种简洁优雅的数据结构 (当然转为维护差分数组的话就反过来了)  

树状数组通常用于维护符合结合律的数据(其实最值维护不好处理)  

两种操作时间复杂度logn

## 模板

:::code-group

```cpp
template <typename T>
struct Fenwick {
    int n;
    std::vector<T> a;
    Fenwick(int n_ = 0) {
        init(n_);
    }
    void init(int n_) {
        n = n_;
        a.assign(n, T{});
    }
    void add(int i, const T &v) {
        while(i<n) {
            a[i]+=v;
            i+=i&-i;
        }
    }
    T get(int i) {
        T ans{};
        while(i>0){
            ans+=a[i];
            i-=i&-i;
        }
        return ans;
    }
    T range(int l, int r) {
        return get(r)-get(l-1);
    }
    int selectKth(const T &k) {
        int x = 0;
        T cur{};
        for (int i = 1 << std::__lg(n); i; i /= 2) {
            if (x + i <= n && cur + a[x + i - 1] <= k) {
                x += i;
                cur = cur + a[x - 1];
            }
        }
        return x;
    }
};
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