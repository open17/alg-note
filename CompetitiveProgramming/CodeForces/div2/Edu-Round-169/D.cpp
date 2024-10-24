/**
 * @title: Colored Portals
 * @desc: ..
 * @tag: 思维/状压
 * @url:
 */

#include <bits/stdc++.h>

/*
 *
 *   宏定义模板常量:
 *
 *          使用STD
 *          重复数据读入
 *          int强制转ll
 *          重载工具函数
 *          启用debug输出
 *          关闭输入同步流
 *          使用文件输入流
 *          使用文件输出流
 *
 */

#define USE_STD
#define USE_LL
#define REAP_READ
#define USE_TOOL
// #define USE_DEBUG
// #define USE_IOS
// #define IN_FILE "data.in"
// #define OUT_FILE "solve.out"

#ifdef USE_STD
using namespace std;
#endif

#ifdef USE_LL
#define int long long
#endif

// 辅助宏
#define rep(i, l, r) for (int i = (l); i < (r); i++)
#define _rep(i, l, r) for (int i = (l); i >= (r); i--)
#define all(x) (x).begin(), x.end()
#define endl '\n' // 避免刷新缓冲区
#define inf32 0x3f3f3f3f
#define max32 INT_MAX

// 类型别名
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128;
using pii = std::pair<int, int>;

// 常规输出
template <typename T>
void print(const T &t) { std::cout << t << endl; }
template <typename T, typename... Args>
void print(const T &t, const Args... args)
{
    std::cout << t << ' ';
    print(args...);
}

// USE_DEBUG 模式下的输出
template <typename T>
void debug(const T &t)
{
#ifdef USE_DEBUG
    std::cout << t << "\n";
#endif
}
template <typename T, typename... Args>
void debug(const T &t, const Args... args)
{
#ifdef USE_DEBUG
    std::cout << t << ' ';
    debug(args...);
#endif
}

#ifdef USE_TOOL
i64 ceilDiv(i64 n, i64 m)
{
    if (n >= 0)
    {
        return (n + m - 1) / m;
    }
    else
    {
        return n / m;
    }
}

i64 floorDiv(i64 n, i64 m)
{
    if (n >= 0)
    {
        return n / m;
    }
    else
    {
        return (n - m + 1) / m;
    }
}

template <class T>
void chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
    }
}

i128 gcd(i128 a, i128 b)
{
    return b ? gcd(b, a % b) : a;
}
#endif

// 快读快写
int read();
void write(int);

const int N = 5e5 + 5;
const int MOD = 1e9 + 7;

int get(char c)
{
    if (c == 'B')
        return 0;
    if (c == 'G')
        return 1;
    if (c == 'R')
        return 2;
    return 3;
}

void solve()
{
    int n = read() + 1, q = read();

    int m = 2 << 4;
    vector<vector<int>> a(n, vector<int>(m, 0)), b(n, vector<int>(m, 0));
    vector<int> arr(n);
    // print(21);
    rep(i, 1, n)
    {
        string s;
        cin >> s;
        // print(s);
        arr[i] = (1 << get(s[0])) | (1 << get(s[1]));
        rep(j, 0, m)
        {
            if (arr[i - 1] == j)
                a[i][j] = i - 1;
            else
                a[i][j] = a[i - 1][j];
        }
    }
    // print(111);
    _rep(i, n - 2, 1)
    {
        rep(j, 0, m)
        {
            if (arr[i + 1] == j)
                b[i][j] = i + 1;
            else
                b[i][j] = b[i + 1][j];
        }
    }
    rep(t_, 0, q)
    {
        int x = read(), y = read();
        if (arr[x] & arr[y])
        {
            print(abs(x - y));
            continue;
        }
        int ans = inf32;
        rep(i, 0, m)
        {
            if ((i & arr[x]) > 0 && i != arr[x])
            {
                if (a[x][i])
                    ans = min(ans, x - a[x][i] + abs(a[x][i] - y));
                if (b[x][i])
                    ans = min(ans, b[x][i] - x + abs(b[x][i] - y));
            }
            if ((i & arr[y]) > 0 && i != arr[y])
            {
                if (a[y][i])
                    ans = min(ans, y - a[y][i] + abs(a[y][i] - x));
                if (b[y][i])
                    ans = min(ans, b[y][i] - y + abs(b[y][i] - x));
            }
        }
        if (ans == inf32)
            print(-1);
        else
            print(ans);
    }
}

signed main()
{
    int T = 1;
#ifdef IN_FILE
    freopen(IN_FILE, "r", stdin);
#endif

#ifdef OUT_FILE
    freopen(OUT_FILE, "w", stdout);
#endif

#ifdef REAP_READ
    std::cin >> T;
#endif

#ifdef USE_IOS
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
#endif

    while (T--)
    {
        solve();
    }
    return 0;
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
inline void write(int x)
{
    if (x < 0)
    {
        putchar('-');
        x = -x;
    }
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}