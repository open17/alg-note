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
#define REAP_READ
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
    std::cout << t << "\n"; 
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

const int N = 5e5 + 5;
const int MOD = 1e9 + 7;

void solve()
{
    int n=read();
    int a[n];
    rep(i,0,n)a[i]=read();
    int b[n+5],c[n+5];
    b[0]=0;
    rep(i,0,n-1){
        if(i==0 || a[i]-a[i-1]>a[i+1]-a[i]){
            b[i+1]=b[i]+1;
        }
        else{
            b[i+1]=b[i]+a[i+1]-a[i];
        }
        debug(b[i+1]);
    }
    debug("------");
    c[n-1]=0;
    _rep(i,n-1,1){
        if(i==n-1 || a[i]-a[i-1]<a[i+1]-a[i]){
            c[i-1]=c[i]+1;
        }
        else{
            c[i-1]=c[i]+a[i]-a[i-1];
        }
        debug(c[i-1]);
    }
    debug("------");
    int m=read();
    rep(i,0,m){
        int x=read()-1,y=read()-1;
        if(x<y){
            print(b[y]-b[x]);
        }
        else{
            print(c[y]-c[x]);
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

