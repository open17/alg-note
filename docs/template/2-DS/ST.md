# ST表

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

<<< @/../template/DS/ST.py [py]

:::