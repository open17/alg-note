#include <bits/stdc++.h>
using namespace std;

#define int long long

#define all(x) (x).begin(), x.end()
#define endl '\n'
#define inf32 0x3f3f3f
#define intf64 1LL << 60

using pii = pair<int, int>;

template <typename T>
void print(const T &t)
{
    cout << t << endl;
}
template <typename T, typename... Args>
void print(const T &t, const Args... args)
{
    cout << t << ' ';
    print(args...);
}

inline int read()
{
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9')
    {
        if (ch == '-')
        {
            f = -1;
        }
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9')
    {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}

void solve(){
    
}

signed main()
{
    int TTT = read();
    while (TTT)
    {
        solve();
        TTT--;
    }
}