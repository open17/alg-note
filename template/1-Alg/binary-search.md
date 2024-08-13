# 二分

## 什么是?

二分查找,利用数据内在的某种有序性(至少满足二段性),从而加速枚举的速度,是非常常用的基本算法之一,也就是说:

一个枚举操作为O(n),而二分可以将操作转为log(n),从而大大缩短时间复杂度

最基本的二分算法当然是直接寻找满足性质的数组上的某个数,一般语言都会内置相关函数：

:::code-group
```cpp
lower_bound(start,end,target);
```

```py
from bisect import bisect_left
bisect_left(nums,target)
```

:::

## 二分答案

解题的一种常见的特殊策略为枚举全部可能得答案并检验是否正确,复杂度为: $O(n*F(t))$,其中$F(t)$为验证答案所需的时间复杂度

还记得上面说的吗,二分是枚举的优化!

所以若答案满足二段性,我们则可以进行二分加速枚举,这样复杂度转为: $O(log(n)*F(t))$


## 浮点二分


浮点二分则为寻找一个满足要求的浮点值,一般用于数学公式找一些特殊点的近似值(比如零点)

因为只需把相等改为浮点误差(一般为目标精度+2),同时不必在意left和right的开闭了,然后对一个公式二分即可



## 注意...

二分的前提是具备**二段性**

注意二分的**边界**,有时候题目在某段边界才满足二段性,所以左指针右指针不要无脑0和inf


## 模板

::: code-group

```cpp
template <typename T>
struct BisectAns{
    T l,r;
    double eps;
    BisectAns(T l,T r){
        setRange(l,r);
        setEps(0);
    }
    BisectAns(T l,T r,double eps){
        setRange(l,r);
        setEps(eps);
    }
    void setRange(T l,T r){
        this->l=l;
        this->r=r;
    }
    void setEps(double eps){
        this->eps=eps;
    }
    T find(auto *p){
        while(r-l>eps){
            T mid=l+(r-l)/2;
            if(p->check(mid))r=mid;
            else l=mid+1;
        }
        return l;
    }
    T find(T (*check)(T v)){
        while(r-l>eps){
            T mid=l+(r-l)/2;
            if(check(mid))r=mid;
            else l=mid+1;
        }
        return l;
    }
};
```

```py
def check(v):
    return 1
l,r=0,n
while l<r:
    mid=l+r>>1
    if check(mid)<target:
        l=mid+1
    else:
        r=mid
print(l)
```

:::
