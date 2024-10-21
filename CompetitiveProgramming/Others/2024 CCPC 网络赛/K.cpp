#include <bits/stdc++.h>
#define int long long
#define ll long long
#define endl '\n'
#define pii pair<int, int>
using namespace std;

template <typename T>
void print(const T &t)
{
    cout << t << endl;
}

template <typename T, typename... Args>
void print(const T &t, const Args... args)
{
    cout << t << " ";
    print(args...);
}

ll qpow(ll a, ll n, ll mod)
{
    ll ans = 1;
    a %= mod;
    while (n)
    {
        if (n & 1)
            ans = (ans * a) % mod;
        a = (a * a) % mod;
        n >>= 1;
    }
    return ans;
}

ll inv(ll a, ll mod)
{
    return qpow(a, mod - 2, mod);
}

int read()
{
    int x = 0, f = 1;
    char c = getchar();
    while (c < '0' || c > '9')
    {
        if (c == '-')
            f = -1;
        c = getchar();
    }
    while (c <= '9' && c >= '0')
    {
        x = x * 10 + (c - '0');
        c = getchar();
    }
    return x * f;
}

bool isAlice(int n, int k)
{
    if (n <= k)
        return true;
    if (n % 2 != 0)
        return true;
    if(k==1)return false;
    if ((n / 2) % 2 != 0)
        return true;
    int s = n / 2;
    int m = k / 2;
    if (k & 1)
        m = (k - 1) / 2;
    return isAlice(s, m);
}

void solve()
{
    int n = read(), k = read();
    if(isAlice(n,k)){
        print("Alice");
    }
    else print("Bob");
}

signed main()
{
    int T = read();
    while (T--)
        solve();
    return 0;
}