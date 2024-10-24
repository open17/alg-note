#include <bits/stdc++.h>
using namespace std;

void solve()
{
    vector<int> v;
    int t;
    cin >> t;
    v.push_back(t);
    for (int i = 1; i < 32; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(), v.end());
    int rank = lower_bound(v.begin(), v.end(), t) - v.begin();
    rank = 32 - rank;
    if (rank == 1)
        cout << 1 << endl;
    else if (rank <= 5)
        cout << 2 << endl;
    else if (rank <= 19)
        cout << 4 << endl;
    else if (rank <= 26)
        cout << 8 << endl;
    else if (rank <= 30)
        cout << 16 << endl;
    else
        cout << 32 << endl;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        solve();
    }
}