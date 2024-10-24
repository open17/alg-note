//  记得val下标从1开始,debug了半天,血的教训


#include <bits/stdc++.h>

/*
 *
 *   宏定义模板常量:
 *
 *          使用STD
 *          重复数据读入
 *          int强制转ll
 *          启用debug输出
 *          关闭输入同步流
 *          使用文件输入流
 *          使用文件输出流
 *
 */

#define USE_STD
#define USE_LL
// #define REAP_READ
// #define USE_DEBUG
// #define USE_IOS
#define IN_FILE "data.in"
#define OUT_FILE "solve.out"


#ifdef USE_STD
using namespace std;
#endif

#ifdef USE_LL
#define int long long
#endif


// 辅助宏
#define rep(i, l, r) for (int i = (l); i < (r); i++)
#define _rep(i, l, r) for (int i = (l); i < (r); i++)
#define all(x) (x).begin(), x.end()
#define inf 0x3f3f3f3f
#define endl '\n'  // 避免刷新缓冲区


// 类型别名
using i64 = long long;
using u64 = unsigned long long;
using pii = std::pair<int, int>;


// 常规输出
template <typename T> void print(const T &t) { std::cout << t << endl; }
template <typename T, typename... Args> void print(const T &t, const Args... args)
{
    std::cout << t << ' ';
    print(args...);
}

// USE_DEBUG 模式下的输出
template <typename T> void debug(const T &t) { 
    #ifdef USE_DEBUG
    std::cout << t << "\n\n ---DEBUG OUTPUT--- \n\n"; 
    #endif
}
template <typename T, typename... Args> void debug(const T &t, const Args... args)
{
    #ifdef USE_DEBUG
    std::cout << t << ' ';
    debug(args...);
    #endif
}

// 快读快写
int read();
void write(int);

const int N = 1e5 + 5;
const int MOD = 1e9 + 7;

int val[N];
int node[N << 2], todo[N << 2];

void _do(int p, int size, int v)
{
    node[p] += v * size;
    todo[p] += v;
}

void _down(int p, int l, int r)
{
    if (l >= r)
        return;
    int size = r - l + 1;
    _do(p * 2, size - size / 2, todo[p]);
    _do(p * 2 + 1, size / 2, todo[p]);
    todo[p] = 0;
}

void _up(int p)
{
    node[p] = node[p * 2] + node[p * 2 + 1];
}

void build(int p, int l, int r)
{
    if (l == r)
    {
        node[p] = val[l];
        return;
    }
    int mid = (l + r) >> 1;
    build(p * 2, l, mid);
    build(p * 2 + 1, mid + 1, r);
    _up(p);
}

void update(int p, int l, int r, int L, int R, int v)
{
    if (L <= l and r <= R)
    {
        _do(p, r - l + 1, v);
        return;
    }
    int mid = (l + r) >> 1;
    _down(p, l, r);
    if (mid >= L)
        update(p * 2, l, mid, L, R, v);
    if (mid < R)
        update(p * 2 + 1, mid + 1, r, L, R, v);
    _up(p);
}

i64 query(int p, int l, int r, int L, int R)
{
    if (L <= l and r <= R)
    {
        return node[p];
    }
    _down(p, l, r);
    i64 ans = 0;
    int mid = (l + r) >> 1;
    if (mid >= L)
        ans += query(p * 2, l, mid, L, R);
    if (mid < R)
        ans += query(p * 2 + 1, mid + 1, r, L, R);
    return ans;
}

void solve()
{
    int n=read(),m=read();
    int a[n];
    rep(i,0,n){
        a[i]=read();
    }
    val[1]=a[0];
    rep(i,1,n){
        val[i+1]=a[i]-a[i-1];
    }
    build(1,1,n);
    rep(i,0,m){
        int opt=read();
        if(opt==1){
            int l=read(),r=read(),k=read(),d=read();
            update(1,1,n,l,l,k);
            if(l+1<=r)update(1,1,n,l+1,r,d);
            if(r+1<=n)update(1,1,n,r+1,r+1,-(k+(r-l)*d));
        }
        else{
            int p=read();
            print(query(1,1,n,1,p));
        }
    }
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

