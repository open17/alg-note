# 快速幂

## 什么是?

基于倍增的算法

## 实现

```cpp
int qpow(int a,int b,int p){
    a%=p;
    int ans=1;
    while(b){
        if(b&1)ans=(ans*a)%p;
        a=(a*a)%p;
        b>>=1;
    }
    return ans;
}
```