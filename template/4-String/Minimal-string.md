# 最小表示法

## 什么是

用于求S的[循环同构](https://oi-wiki.org/string/minimal-string/#%E5%BE%AA%E7%8E%AF%E5%90%8C%E6%9E%84)串的最小字典序

时间复杂度$O(n)$

## 如何

> 引自OI WIKI

- 初始化指针 i 为 0，j 为 1；初始化匹配长度 k 为 0
- 比较第 k 位的大小，根据比较结果跳转相应指针。若跳转后两个指针相同，则随意选一个加一以保证比较的两个字符串不同
- 重复上述过程，直到比较结束
- 答案为 i,j 中较小的一

## 模板

[例题](https://www.luogu.com.cn/problem/P1368)

```cpp
int n=read();
int a[n*2];
For(i,0,n){
    a[i]=read();
    a[i+n]=a[i];
}
int i=0,j=1,k=0;
while(i<n&&j<n){
    while(a[i+k]==a[j+k])k++;
    if(a[i+k]>a[j+k])i+=k+1;
    else j+=k+1;
    k=0;
    if(i==j)j++;
}
int st=min(i,j);
For(i,st,st+n){
    char f=' ';
    if(i==st+n-1)f=endl;
    cout<<a[i]<<f;
}
```