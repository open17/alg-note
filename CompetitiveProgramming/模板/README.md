# 算法模板

## 赛前准备

- 学生证
- 草稿纸与笔

## 注意事项

- 仔细看题，不要看漏看错看反
- 注意条件与数据，思考时间复杂度与猜测算法
- 尝试转化问题为相似已知问题
- 尝试多手玩/打表，找性质与规律
- 没思路时，多想什么题目条件没用上
- 尝试构造一些常见的性质，比如单调性
- 也从暴力枚举开始思考优化
- 或者正难则反
- 或者从简化版的题目开始思考
- 或者思考贡献

## 火车头

```cpp

#include <bits/stdc++.h>
using namespace std;


#define int long long


#define all(x) (x).begin(), x.end()
#define endl '\n'  // 避免刷新缓冲区
#define inf32 0x3f3f3f3f
#define inf64 1LL << 60
#define max32 INT_MAX
#define max64 LONG_LONG_MAX


// 类型别名
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128;
using pii = std::pair<int, int>;

// 常规输出
template <typename T> void print(const T &t) { std::cout << t << endl; }
template <typename T, typename... Args> void print(const T &t, const Args... args)
{
    std::cout << t << ' ';
    print(args...);
}

i64 ceilDiv(i64 n, i64 m) {
    if (n >= 0) {
        return (n + m - 1) / m;
    } else {
        return n / m;
    }
}
 
i64 floorDiv(i64 n, i64 m) {
    if (n >= 0) {
        return n / m;
    } else {
        return (n - m + 1) / m;
    }
}

template<class T>
void chmax(T &a, T b) {
    if (a < b) {
        a = b;
    }
}

template <class T>
void chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
    }
}

inline int read()
{
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9')
    {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9')
    {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}
```

