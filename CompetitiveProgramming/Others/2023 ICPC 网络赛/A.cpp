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
#define endl '\n'  // 避免刷新缓冲区
#define inf32 0x3f3f3f3f
#define inf64 1LL << 60
#define max32 INT_MAX


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

// USE_DEBUG 模式下的输出
template <typename T> void debug(const T &t) { 
    #ifdef USE_DEBUG
    std::cout << t << "\n\n"; 
    #endif
}
template <typename T, typename... Args> void debug(const T &t, const Args... args)
{
    #ifdef USE_DEBUG
    std::cout << t << ' ';
    debug(args...);
    #endif
}

#ifdef USE_TOOL
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


template <class T>
T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
#endif

// 快读快写
int read();
void write(int);

const int N = 5e5 + 5;
const int MOD = 1e9 + 7;

struct Res{
    string name;
    pii val;
    Res(string name,pii val){
        this->name=name;
        this->val=val;
    }
};

bool compare(const Res& a, const Res& b) {
    int A=min(a.val.first,a.val.second);
    int B=min(b.val.first,b.val.second);
    if(A==B)return a.val.first< b.val.first; 
    return A < B;
}


void solve()
{
    int n=read(),m=read();
    unordered_map<string,pii> mp;
    set<string> ss;
    string s;
    rep(i,0,n){
        cin>>s;
        if(!mp.count(s))mp[s]={(int)mp.size()+1,inf32};
    }
    rep(i,0,m){
        cin>>s;
        ss.insert(s);
        if(!mp.count(s))mp[s]={inf32,(int)ss.size()};
        else mp[s].second=min(mp[s].second,(int)ss.size());
    }
    vector<Res> ans;
    for(auto p:mp){
        Res tmp(p.first,p.second);
        ans.push_back(tmp);
    }
    sort(all(ans),compare);
    for(auto a:ans)print(a.name);
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