# ST表

## 什么是


利用倍增思想维护区间最值信息

## 模板

:::code-group

```cpp
int A[N], f[__lg(N) + 1][N];
void init(int n) {
    for (int i = 1; i <= n; ++i)
        f[0][i] = A[i];
    for (int i = 1; i <= __lg(n); ++i)
        for (int j = 1; j + (1 << i) - 1 <= n; ++j)
            f[i][j] = max(f[i - 1][j], f[i - 1][j + (1 << (i - 1))]);
}
int query(int l, int r) {
    int s = __lg(r - l + 1);
    return max(f[s][l], f[s][r - (1 << s) + 1]);
}
```

```py
import math

def init_st(arr):
    n=len(arr)
    logn=int(math.log2(n+1)) + 1
    st=[[0] * logn for _ in range(n+1)]
    for i in range(1, n+1):
        st[i][0]=arr[i]
    for j in range(1, logn):
        for i in range(1, n+1):
            if i+(1<<j)-1<=n:
                st[i][j]=min(st[i][j-1],st[i+(1<<(j-1))][j-1])
    return st

def query_st(st, left, right):
    length=right-left+1
    k=int(math.log2(length))
    return min(st[left][k], st[right-(1<<k)+1][k])
```

:::