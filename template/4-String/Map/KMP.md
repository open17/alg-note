# KMP

## 什么是?

用于匹配字符串

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e6 + 5;
int pmt[MAXN];
void get_pmt(const string& s) {
    for (int i = 1, j = 0; i < s.length(); ++i) {
        while (j && s[i] != s[j]) j = pmt[j - 1];
        if (s[i] == s[j]) j++;
        pmt[i] = j;
    }
}
void kmp(const string& s, const string& p) {
    for (int i = 0, j = 0; i < s.length(); ++i) {
        while (j && s[i] != p[j]) j = pmt[j - 1];
        if (s[i] == p[j]) j++;
        if (j == p.length()) {
            cout << i - j + 2 << '\n'; // 因为要1-index，所以是+2
            j = pmt[j - 1];
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    string s, p;
    cin >> s >> p;
    get_pi(p);
    kmp(s, p);
    for (int i = 0; i < p.length(); ++i)
        cout << pmt[i] << ' ';
    return 0;
}
```

