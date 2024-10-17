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

struct custom_hash
{
    static uint64_t splitmix64(uint64_t x)
    {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const
    {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int read();
void write(int);

const int N = 250000 + 5;
const int MOD = 1e9 + 7;
int T = 1;

int cnt = 0;
int nxt[N][4][3];
int tol[N];

int get(char c){
    if(c=='A')return 0;
    if(c=='C')return 1;
    if(c=='T')return 2;
    return 3;
}

void insert()
{
    string s;
    cin >> s;
    int cur = 0;
    for (int i = 0; i < s.size(); i++)
    {
        // print(cur);
        int c = get(s[i]);
        if (!nxt[cur][c][0])
        {
            nxt[cur][c][0] = ++cnt;
        }
        if (i == s.size() - 1)
            nxt[cur][c][1]++;
        cur = nxt[cur][c][0];
        tol[cur]++;
    }
}

int dfs(int cur, string s, int i)
{
    int c = get(s[i]);
    if (i == s.size() - 1)
    {
        if (s[i] == '*')
        {
            return tol[cur];
        }
        if (s[i] == '?')
        {
            int ans=0;
            For(c, 0, 4)
            {
                if (nxt[cur][c][1])
                    ans++;
            }
            return ans;
        }
        return nxt[cur][c][1];
    }

    if (s[i] == '*')
    {
        int ans = dfs(cur, s, i + 1);
        For(c, 0, 4)
        {
            if (nxt[cur][c][0])
            {
                ans += dfs(nxt[cur][c][0], s, i);
            }
        }
        return ans;
    }

    if (s[i] == '?')
    {
        // print(i,s[i],nxt[cur]['T'-'A'][1]);
        int ans=0;
        For(c, 0, 4)
        {
            if (nxt[cur][c][0])
            {
                // print(c);
                ans += dfs(nxt[cur][c][0], s, i+1);
            }
        }
        return ans;
    }

    // print(nxt[cur][c][0],s[i],cur);
    return dfs(nxt[cur][c][0], s, i + 1);
}

void hhhh()
{
    string s;
    cin >> s;
    int n = read();
    For(i, 0, n)
    {
        insert();
    }
    print(n-dfs(0, s, 0));
}

signed main()
{
    // 单个时关闭cin即可
    // cin >> T;
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
