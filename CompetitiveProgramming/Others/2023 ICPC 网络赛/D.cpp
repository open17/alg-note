/**
 * @title: ..
 * @desc: ..
 * @tag: IO
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
// #define REAP_READ
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
#define inf64 1LL << 60
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
    std::cout << t << "\n\n";
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

template <class T>
void chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
    }
}

template <class T>
T gcd(T a, T b)
{
    return b ? gcd(b, a % b) : a;
}
#endif

// 快读快写
int read();
void write(int);

const int N = 5e5 + 5;
const int MOD = 1e9 + 7;

struct DSU
{
    std::vector<int> f, siz, edge_siz;

    DSU() {}
    DSU(int n)
    {
        init(n);
    }

    void init(int n)
    {
        f.resize(n);
        std::iota(f.begin(), f.end(), 0);
        siz.assign(n, 1);
        edge_siz.assign(n, 0);
    }

    int find(int x)
    {
        while (x != f[x])
        {
            x = f[x] = f[f[x]];
        }
        return x;
    }

    bool same(int x, int y)
    {
        return find(x) == find(y);
    }

    bool merge(int x, int y)
    {
        x = find(x);
        y = find(y);
        edge_siz[x]++;
        if (x == y)
        {
            return false;
        }
        edge_siz[x] += edge_siz[y];
        siz[x] += siz[y];
        f[y] = x;
        return true;
    }
    int edge_size(int x)
    {
        return edge_siz[find(x)];
    }
    int size(int x)
    {
        return siz[find(x)];
    }
};

void solve()
{
    int n = read(), m = read();

    DSU dsu(n + 1);
    int id1 = -1, id2 = -2, s1 = inf32, s2 = inf32;
    rep(i, 0, m)
    {
        int u = read(), v = read();
        dsu.merge(u, v);
    }
    unordered_map<int,pii> um;
    rep(u, 1, n + 1)
    {
        int idx = dsu.find(u);
        int len = dsu.size(u);
        int elen = dsu.edge_size(u);
        um[idx]={len,elen};
        if (idx == id1)
        {
            s1 = len;
        }
        else if (idx == id2)
        {
            s2 = len;
        }
        else if (len < s1)
        {
            id2 = id1;
            s2 = s1;
            s1 = len;
            id1 = idx;
        }
        else if (len < s2)
        {
            id2 = idx;
            s2 = len;
        }
        if (s1 > s2)
        {
            id2 ^= id1;
            id1 ^= id2;
            id2 ^= id1;
            s2 ^= s1;
            s1 ^= s2;
            s2 ^= s1;
        }
    }
    int ans=0;
    for(auto p:um){
        int nn=p.second.first;
        int mm=p.second.second;
        ans+=(nn-1)*nn/2-mm;
    }
    if(ans!=0)print(ans);
    else print(s1 * s2);
}

signed main()
{
    int T = 1;
    debug("hello world");
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