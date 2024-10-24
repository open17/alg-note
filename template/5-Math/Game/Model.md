# 经典博弈模型

尽管现在出现频率很低（现在很多猜奇偶），但是依然有一定的启发意义

## 巴什博弈

对于n个物品可以取1~k个，轮流取，不能取的输，何时先手必胜？

结论：n%(k+1)!=0

余数证明一下就行

## Nim博弈

对于$k$个堆，每堆有$a_k$个物品，每次可以选任意一堆取任意个，轮流取，不能取的输，何时先手必胜？

结论：每堆物品的异或和不等于0时先手必胜

证明比较复杂，不过这个模型算是这三个中最有意义的，SG定理也是由此推导的

## 威佐夫博弈

有两堆各若干个物品，两个人轮流从任意一堆中取出至少一个或者同时从两堆中取出同样多的物品，规定每次至少取一个，至多不限，不能取的输，何时先手必胜？

非奇异局势先手必胜

奇异局势规律： 两堆数量差值*1.618等于小堆的值

```cpp
void solve()
{
    int a=read(),b=read();
    long double x=abs(b-a);
    long double y=(sqrtl(5.0)+1)/2;
    int p=x*y;
    if(min(a,b)==p)print(0);
    else print(1);
}
```