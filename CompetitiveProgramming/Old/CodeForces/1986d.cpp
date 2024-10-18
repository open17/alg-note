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

int query(int l, int r, int h[], int p[])
{
    l++;
    r++;
    return h[r] - h[l - 1] * p[r - l + 1];
}

int f(int i, int j, int h[], int p[], int cnt)
{
    if (i == 0)
    {
        if (cnt != 0)
            return -1;
        int q = query(i, j, h, p);
        if (q == 1)
            return 0;
        return q;
    }

    if (cnt == 0)
    {
        return f(0, j, h, p, 0);
    }
    int ans = f(i - 1, j, h, p, cnt);
    int res = f(i - 1, i - 1, h, p, cnt - 1);
    int q = query(i, j, h, p);
    if (!(q == 1 && res >= 0))
    {
        res += q;
    }
    // print(i,j,cnt,ans,res);
    int ret = -1;
    if (ans <= -1)ret = res;
    else if (res <= -1)ret = ans;
    else ret = min(ans, res);
    return ret;
}

void hhhh()
{
    int n = read();
    string s;
    cin >> s;
    if (n <= 2)
    {
        if (n == 2 && s[0] == '0')
            print(s[1]);
        else
            print(s);
        return;
    }
    if (n == 3)
    {
        if (s[0] == '0' || s[n - 1] == '0')
        {
            print(0);
            return;
        }
        if (s == "101")
        {
            print(1);
            return;
        }
    }
    if (n > 3)
    {
        For(i, 0, n)
        {
            if (s[i] == '0')
            {
                print(0);
                return;
            }
        }
    }
    int p[n + 5], h[n + 5];
    const int BASE = 10;
    p[0] = 1;
    h[0] = 0;
    For(i, 1, n + 1)
    {
        p[i] = (p[i - 1] * BASE);
        h[i] = (h[i - 1] * BASE + (s[i - 1] - '0'));
    }
    int ans = f(n - 1, n - 1, h, p, n - 2);
    print(ans);
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
