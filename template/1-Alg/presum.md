# 前缀和与差分

## 定义
使用O(n)的时间预处理,然后将后续的查询/操作转为O(1)的复杂度

前缀和可以支持O(1)的区间查询

差分支持O(1)的区间修改

## 重点

- 也常用于操作转换(区间转单点,单点转区间)
- 注意差分思想不局限于维护加减,实际上可以维护具备结合律的关系,比如异或关系

## 一维

:::code-group

```cpp
template <typename T>
struct Presum{
    vector<T> a;
    int n;
    Presum(int n_=0){
       init(n_);
    }
    Presum(vector<T> &b){
       presum(b);
    }
    void presum(vector<T> &b){
        init(b.size()+1);
        for(int i=1;i<n;i++){
            a[i]=a[i-1]+b[i-1];
        }
    }
    void init(int n_) {
        n = n_;
        a.assign(n, T{});
    }
    T sum(){
        for(int i=1;i<=n;i++){
            a[i]+=a[i-1];
        }
    }
    T get(int i){
        return a[i];
    }
    T getRange(int l,int r){
        return a[r]-a[l-1];
    }
    void add(int i, const T &v) {
        a[i]+=v;
    }
    void addRange(int l,int r,const T &v){
        add(l,v);
        add(r+1,-v);
    }
};
```

```py
from itertools import accumulate
b = list(accumulate(a, initial=0))

def update(l,r):
    b[l]+=c
    b[r+1]-=c
```

:::

## 二维 

手推容斥即可

:::code-group

```cpp
const int N = 150;
int a[N][N];

int get(int x1, int y1, int x2, int y2)
{
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1];
};

int n = read();
memset(a, 0, sizeof(a));

For(i, 1, n + 1)
{
    For(j, 1, n + 1)
    {
        a[i][j] = read();
        a[i][j] += a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1];
    }
}

void update(int x1,int y1,int x2,int y2,int v){
    x2++;
    y2++;
    a[x1][y1]+=v;
    a[x2][y1]-=v;
    a[x1][y2]-=v;
    a[x2][y2]+=v;
    
}
```

```py
def init(n,m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            a[i][j] +=a[i-1][j] + a[i][j-1] - a[i-1][j-1]
            
def get(x1,y1,x2,y2):
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]

def update(x1, y1,x2,y2 val):
    x2+=1
    y2+=1
    a[x1][y1] += val
    a[x2][y2] += val
    a[x1][y2] -= val
    a[x2][y1] -= val
```

:::

## 更多

[集训题解课件](https://slides.open17.vip/slides/ACM2024-SUMMER/)
