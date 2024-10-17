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
    int n = read();
    int a[n], b[n];
    For(i, 0, n) a[i] = read();
    For(i, 0, n) b[i] = read();
    int fa = 0, fb = 0, v1 = 0,v2=0;
    For(i, 0, n)
    {
        if (a[i] == 1 && b[i] == 1)
            v1++;
        else if (a[i] == -1 && b[i] == -1)
            v2--;
        else if (a[i] > b[i])
            fa += a[i];
        else if (a[i] < b[i])
            fb += b[i];
    }

    // print(fa, fb, v);

    // keep fa>=fb

    if (fa < fb)
    {
        int tmp = fb;
        fb = fa;
        fa = tmp;
    }

    int dif = abs(fa - fb);

    // print("DIF",dif,fa,fb,v1,v2);

    if(dif>0){
        fb += min(dif, v1);
        v1 -= min(dif, v1);
    }

    dif=abs(fa-fb);
    if(dif>0){
        fa -= min(dif, -v2);
        v2 += min(dif, -v2);
    }

    int v=v1+v2;

    // print("DIF2",dif,fa,fb,v1,v2);

    if (v == 0)
        print(min(fa, fb));
    else
    {
        // print(v,ceil(((double)-v) / 2));
        if (v >= 0)
            print(fa + v / 2);

        else
            print(fa - ceil(((double)-v) / 2));
    }
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
