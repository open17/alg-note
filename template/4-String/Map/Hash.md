# 字符串哈希

## 什么是?

定义多项式 Hash 函数：

$$f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$$

我们可以通过该函数将字符串映射为b进制下的数字

同时我们可以预处理储存所有的前缀，然后便可以$O(1)$得到任意子串的Hash值

## 模板

:::code-group

```cpp
struct StrHash{
    int MOD,BASE,n;
    vector<int> p,h;
    StrHash(int n_=0){
        randing();
        init(n_);
    }
    StrHash(string s){
        randing();
        init(s.size());
        work(s);
    }
    void init(int n_){
        n=n_+1;
        p.assign(n, int{});
        h.assign(n, int{});
        p[0]=1;
        h[0]=0;
    }
    void randing(){
        srand(time(0));
        MOD = 998244353 + rand() % 10008;
        BASE = 33 + rand() % 234;
    }
    void work(string s){
        for(int i=1;i<n;i++){
            p[i] = ((long long)p[i - 1] * BASE) % MOD; 
            h[i]=((long long)h[i-1]*BASE+s[i-1]-'a')%MOD;
        }
    }
    int get(int l,int r){
        return (h[r] - (long long) h[l-1] * p[r-l+1] % MOD + MOD) % MOD;
    }
};
```

```cpp [cpp未封装版]
int p[N];
int h[N];


int query(int l,int r,int MOD){
    return (h[r] - h[l-1] * p[r-l+1] % MOD + MOD) % MOD;
}

void hhhh()
{
    string s;
    cin >> s;
    int n = s.size();
    srand(time(0));
    const int MOD = 998244353 + rand() % 10008;
    const int BASE = 33 + rand() % 234;
    p[0] = 1;
    h[0] = 0;
    For(i, 1, n + 1) { 
        p[i] = (p[i - 1] * BASE) % MOD; 
        h[i]=(h[i-1]*BASE+s[i-1]-'a')%MOD;
    }
    int m=read();
    For(i,0,m){
        int a=read(),b=read(),c=read(),d=read();
        if(query(a,b,MOD)==query(c,d,MOD))print("Yes");
        else print("No");
    }
}
```

```py
import random

s = input()
n = len(s)

random.seed()
MOD1 = 998244353 + random.randint(0, 10007)
MOD2 = int(1e9+7) + random.randint(0, 233)
BASE1 = 33 + random.randint(0, 233)
BASE2 = 133 + random.randint(0, 53)

b1 = [1]
b2 = [1]
h1 = [0]
h2 = [0]

for i in range(n):
    b1.append(b1[i] * BASE1 % MOD1)
    b2.append(b2[i] * BASE2 % MOD2)
    h1.append((h1[i] * BASE1 % MOD1 + ord(s[i]) - ord('a')) % MOD1)
    h2.append((h2[i] * BASE2 % MOD2 + ord(s[i]) - ord('a')) % MOD2)  

# 从0开始,左闭右闭
def query(l, r):
    hash1 = (h1[r + 1] - h1[l] * b1[r - l + 1] % MOD1 + MOD1) % MOD1
    hash2 = (h2[r + 1] - h2[l] * b2[r - l + 1] % MOD2 + MOD2) % MOD2
    return hash1, hash2
```

:::

## 例题

幽默一刻:![被卡掉](https://cdn.jsdelivr.net/gh/open17/Pic/img/202404121358256.png)

单随机模数和BASE中奖,给测试用例卡掉了,再提交一遍不改代码就过了

```py
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        思维转换
        """
        # 最坏情况
        
        s=word
        # 哈希板子
        n=len(s)
        ans=ceil(n/k)

        random.seed()
        MOD1 = 998244353 + random.randint(0, 10007)
        MOD2 = int(1e9+7) + random.randint(0, 233)
        BASE1 = 33 + random.randint(0, 233)
        BASE2 = 133 + random.randint(0, 53)

        b1 = [1]
        b2 = [1]
        h1 = [0]
        h2 = [0]

        for i in range(n):
            b1.append(b1[i] * BASE1 % MOD1)
            b2.append(b2[i] * BASE2 % MOD2)
            h1.append((h1[i] * BASE1 % MOD1 + ord(s[i]) - ord('a')) % MOD1)
            h2.append((h2[i] * BASE2 % MOD2 + ord(s[i]) - ord('a')) % MOD2)  

        # 从0开始,左闭右闭
        def query(l, r):
            hash1 = (h1[r + 1] - h1[l] * b1[r - l + 1] % MOD1 + MOD1) % MOD1
            hash2 = (h2[r + 1] - h2[l] * b2[r - l + 1] % MOD2 + MOD2) % MOD2
            return hash1, hash2


        def check(a,b):
            return query(0,a)==query(b,n-1)

        for t in range(1,ans):
            if check(n-t*k-1,t*k):
                return t
        return ans
            
```
