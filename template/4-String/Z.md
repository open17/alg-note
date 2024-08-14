# Z函数

## 什么是？

国内一般称为扩展KMP，不过个人认为这个思想其实更接近马拉车XD

主要用于求出字符串s与s的后缀的LCP（最长公共前缀）

## 模板

```cpp
std::vector<int> zFunction(std::string s) {
    int n = s.size();
    std::vector<int> z(n + 1);
    z[0] = n;
    for (int i = 1, j = 1; i < n; i++) {
        z[i] = std::max(0, std::min(j + z[j] - i, z[i - j]));
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if (i + z[i] > j + z[j]) {
            j = i;
        }
    }
    return z;
}
```