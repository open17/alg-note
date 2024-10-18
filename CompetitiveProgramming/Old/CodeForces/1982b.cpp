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
    int x = read(), y = read(), k = read();
    vector<int> qp;
    int tmp = 1;
    qp.push_back(tmp);
    while (tmp <= x)
    {
        tmp *= y;
        qp.push_back(tmp);
    }
    if (x % y == 0)
    {
        k--;
        x++;
    }
    while (k)
    {
        if (x == 1)
        {
            x += k % (y - x);
            break;
        }
        int kk = ceil(((double)x) / y);
        int dif = kk * y - x;
        if (k < dif)
        {
            x += k;
            break;
        }
        k -= dif;
        if (x < y)
            x = 1;
        else
        {

            int l = 0, r = qp.size();
            while (l < r)
            {
                int mid = l + (r - l) / 2;
                if (kk % qp[mid] == 0)
                    l = mid + 1;
                else
                    r = mid;
            }
            x = kk / qp[r - 1];
        }
    }
    print(x);
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
