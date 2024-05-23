# 01字典树

## 什么是?
用于解决一些异或问题,也可以用于模拟平衡树(但是我不会)

## 策略
如果我们要找与给定数异或最大的数，就尽可能走与该数当前位不同的路径
反之则尽可能走与当前位相同的路径

::: tip python提示
在python我们通常用数组模拟,python开定长反而可能耗时大
:::
## 模板

:::code-group

```cpp
const int N=3e5+5;
int nxt[N][26][2];
int cnt = 0;
string s;
For(i, 0, n)
{   
    cin >> s;
    int cur = 0;
    for (int i = 0; i < s.size(); i++)
    {
        int c = s[i] - 'a';
        if (!nxt[cur][c][0])
        {
            nxt[cur][c][0] = ++cnt;
        }
        nxt[cur][c][1]++;
        cur = nxt[cur][c][0];
    }
}
```

<<< @/../template/DS/01tire.py

:::