/**
 * @title: Numeric String Template
 * @desc: 我怕map常数的大被卡，就改用离散化
 * @tag: 离散化/思维
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
#define endl '\n'  // 避免刷新缓冲区
#define inf32 0x3f3f3f3f
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

i128 gcd(i128 a, i128 b) {
    return b ? gcd(b, a % b) : a;
}
#endif

// 快读快写
int read();
void write(int);

const int N = 26;
const int MOD = 1e9 + 7;


template <typename T>
struct Discrete{
    vector<T> arr;
    Discrete(){}
    Discrete(vector<T> &arr){
        init(arr);
    }
    void init(vector<T> &arr){
        this->arr=arr;
        clear();
    }
    void add(T val){
        arr.push_back(val);
    }
    void clear(){
        sort(arr.begin(),arr.end());
        arr.erase(unique(arr.begin(),arr.end()),arr.end());
    }
    T get(T v){
        return lower_bound(arr.begin(),arr.end(),v)-arr.begin();
    }
};

void solve()
{
    int n=read();
    vector<int> a(n);
    vector<int> lst_a(N,-1);
    vector<int> lst_s(N,-1);
    rep(i,0,n){
        a[i]=read();
    }
    int m=read();
    Discrete<int> disc(a);
    if(disc.arr.size()>N){
        rep(i,0,m){
            string s;
            cin>>s;
            print("NO");
        }
        return;
    }
    int flag;
    rep(t_,0,m){
        lst_s.assign(N,-1);
        lst_a.assign(N,-1);
        string s;
        cin>>s;
        flag=0;
        if(s.size()!=n)flag=1;
        rep(i,0,n){
            if(lst_s[s[i]-'a']!=lst_a[disc.get(a[i])]){
                flag=1;
                break;
            }
            lst_s[s[i]-'a']=i;
            lst_a[disc.get(a[i])]=i;
        }
        if(!flag){
            print("YES");
        }
        else{
            print("NO");
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