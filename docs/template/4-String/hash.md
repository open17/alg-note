# 字符串哈希

## 什么是?

定义多项式 Hash 函数：

$$f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$$


## 模板

:::code-group

```cpp
// 蒯自蛙总
long long P[n + 1];
P[0] = 1;
for (int i = 1; i <= n; i++)
    P[i] = P[i - 1] * BASE % MOD;
long long H[n + 1];
H[0] = 0;
for (int i = 1; i <= n; i++)
    H[i] = (H[i - 1] * BASE + word[i - 1] - 'a') % MOD;
auto query = [&](int L, int R)
{
    return (H[R] - H[L - 1] * P[R - L + 1] % MOD + MOD) % MOD;
};
```

<<< @/../template/String/hash.py [python 双模数]

:::

## 例题

幽默一刻:![被卡掉](https://cdn.jsdelivr.net/gh/open17/Pic/img/202404121358256.png)

单随机模数和BASE中奖,给测试用例卡掉了,再提交一遍不改代码就过了

<<< @/../code/LeetCode/3031[字符串哈希].py