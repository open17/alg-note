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

void solve()
{
    int n = read();
    vector<int> a(n);
    vector<int> L(n, -1);
    vector<int> R(n, -1);
    for (int i = 0; i < n; i++)
        a[i] = read();
    vector<int> p = a;
    sort(all(p));
    p.erase(unique(all(p)), p.end());
    unordered_map<int, vector<pii>> mp;
    int now = a[0], lst_l = 0;
    for (int i = 0; i < n; i++)
    {
        if (i == n - 1 || a[i + 1] != a[i])
        {
            L[lst_l] = lst_l;
            R[i] = i;
            mp[a[i]].push_back({lst_l, i});
            lst_l = i + 1;
        }
    }
    int ans = 0;
    for (auto pp : p)
    {
        for (auto x : mp[pp])
        {
            int ldx = L[x.first];
            int rdx = R[x.second];
            int len = rdx - ldx + 1;
            if (rdx + 1 >= n && ldx - 1 < 0)
            {
                continue;
            }
            else if (ldx - 1 < 0)
            {
                if (a[rdx] != a[rdx + 1])
                    ans += len;
                a[rdx]=a[rdx+1];
                L[rdx + 1] = ldx;
            }
            else if (rdx + 1 >= n)
            {
                if (a[ldx] != a[ldx - 1])
                    ans += len;
                a[ldx]=a[ldx-1];
                R[ldx - 1] = rdx;
            }
            else if (a[ldx - 1] > a[rdx + 1])
            {
                if (a[rdx] != a[rdx + 1])
                    ans += len;
                a[rdx]=a[rdx+1];
                L[rdx + 1] = ldx;
            }
            else if (a[ldx - 1] <= a[rdx + 1])
            {
                if (a[ldx] != a[ldx - 1])
                    ans += len;
                a[ldx]=a[ldx-1];
                R[ldx - 1] = rdx;
            }
            a[ldx]=max(a[ldx],a[rdx]);
            a[rdx]=max(a[rdx],a[ldx]);
        }
    }
    print(ans);
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