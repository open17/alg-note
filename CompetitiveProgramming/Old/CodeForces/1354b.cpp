#include <bits/stdc++.h>
using namespace std;
#define int long long
#define ios                      \
    ios::sync_with_stdio(false); \
    cin.tie(0);                  \
    cout.tie(0);
#define For(w, a, n) for (int w = (a); w < (n); ++w)
#define _For(a, b, c) for (int a = (b); a > (c); a--)
#define all(x) (x).begin(), x.end()
#define inf 0x3f3f3f3f
#define endl '\n'
// 对拍
#define fo1                         \
    freopen("data.in", "r", stdin); \
    freopen("res.out", "w", stdout);
#define fo2                         \
    freopen("data.in", "r", stdin); \
    freopen("ans.out", "w", stdout);
// 输出
#define printA(a, b, c)            \
    cout << '\n'                   \
         << "debug start" << '\n'; \
    for (int i = a; i <= b; i++)   \
    {                              \
        cout << c[i] << ' ';       \
    }                              \
    cout << "\n\ndebug over\n\n";
template <typename T>
void print(const T &t) { cout << t << endl; }
template <typename T, typename... Args>
void print(const T &t, const Args... args)
{
    cout << t << ' ';
    print(args...);
}
template <typename T>
void println(const T &t) { cout << t << endl; }
template <typename T, typename... Args>
void println(const T &t, const Args... args)
{
    cout << t << endl;
    println(args...);
}

typedef unsigned long long ull;
typedef pair<int, int> pii;
int read();
void write(int);

const int N = 5e5 + 5;
const int MOD = 1e9 + 7;
int T = 1;

void hhhh()
{
    string s;
    cin>>s;
    int a=0,b=0,c=0;
    int l=0,res=INT_MAX;
    for(int i=0;i<s.size();i++){
        if(s[i]=='1')a++;
        else if(s[i]=='2')b++;
        else c++;
        while(a&&b&&c&&l<=i){
            res=min(res,i-l+1);
            if(s[l]=='1')a--;
            else if(s[l]=='2')b--;
            else c--;
            l++;
        }
    }
    if(res==INT_MAX)res=0;
    print(res);
}

signed main()
{
    // 单个时关闭cin即可
    cin >> T;
    while (T--)
    {
        hhhh();
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

