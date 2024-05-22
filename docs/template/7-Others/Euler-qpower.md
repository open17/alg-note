# 欧拉降幂


## 什么是?

欧拉降幂是一种处理模幂运算中底数指数特别大的情况的方法。

欧拉函数记为 $\phi(n)$，它表示小于或等于 $n$ 的正整数中与 $n$ 互质的数的数量。


欧拉降幂基于欧拉定理，该定理指出，如果 $a$ 和 $n$ 互质，则：

$$a^{\phi(n)} \equiv 1 \pmod{n}$$

这意味着当处理 $a^b \pmod{n}$ 时，如果 $b$ 比 $\phi(n)$ 大，我们可以先用 $b$ 除以 $\phi(n)$ 的余数来代替 $b$，因为每经过 $\phi(n)$ 次幂，结果模 $n$ 会恢复为原值。具体实现步骤如下：

1. **计算欧拉函数 $\phi(n)$**：这是整个过程的关键步骤，对于不同的 $n$，计算方式可能会有所不同。如果 $n$ 是质数，$\phi(n) = n - 1$。对于一般情况，需要分解 $n$ 的质因数。

2. **简化指数**：将指数 $b$ 替换为 $b \mod \phi(n)$。如果 $b$ 大于 $\phi(n)$，这可以大幅减少计算量。

3. **模幂计算**：使用快速幂算法计算 $a^{b \mod \phi(n)} \pmod{n}$。


## 实现


[例题](https://leetcode.cn/problems/super-pow/description/)

::: code-group


```cpp
constexpr int Phi(int n) noexcept
{
    int result = n;
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            while (n % i == 0)
            {
                n /= i;
            }
            result -= result / i;
        }
    }
    if (n > 1)
    {
        result -= result / n;
    }
    return result;
}

class Solution
{
public:
    static constexpr int MOD = 1337;
    static constexpr int PHI_M = Phi(MOD);
    int superPow(int a, vector<int> &b)
    {
        int bm = 0;
        for (int i =0; i < b.size() ; i++)
        {
            bm = ((bm * 10)% PHI_M + b[i]% PHI_M) % PHI_M;
        }
        // 这里可以&&上一个判断Phi(MOD)是否小于b的条件加速
        if (gcd(a, MOD) != 1)
            bm += PHI_M;
        cout<<bm<<endl;
        return qpow(a, bm, MOD);
    }
    int qpow(int a, int b, int p)
    {
        int ans = 1;
        while (b)
        {
            if (b & 1)
                ans = ((ans%p) *(a%p)) % p;
            a = ((a%p) * (a%p)) % p;
            b >>= 1;
        }
        return ans;
    }
};
```


```python
def compute_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while (n % p == 0):
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def modular_exponentiation(a, b, n):
    if n == 1:
        return 0
    phi_n = compute_phi(n)
    b = b % phi_n
    result = 1
    a = a % n
    while b > 0:
        if (b % 2 == 1): # 如果b是奇数，将结果乘以当前的a
            result = (result * a) % n
        a = (a * a) % n  # 平方
        b //= 2
    return result

# 例子
a = 3
b = 1000000000
n = 7
print(modular_exponentiation(a, b, n))
```


:::

