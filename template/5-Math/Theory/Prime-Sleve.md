# 素数筛

## 什么是? 

素数筛用于求一段数据范围内那些数为素数

## 如何?

显然暴力的想法为对数据范围内所有数都做一遍素数判定,这种做法是$O(n\sqrt n)$的,效度很低

如何优化呢?注意到一个数的倍数一定为合数,因此我们只需要对每个数标记其倍数即可

这便是埃氏筛,但是这效率依然不高,它会将一个合数重复多次标记

我们可以避免这个重复,使得效率达到线性

## 代码

:::code-group

```py
def prime_sleve(n):
    ans=[]
    is_prime=[True]*(n+1)
    for i in range(2,n+1):
        if is_prime[i]:
            ans.append(i)
        for pri in ans:
            if pri*i>n:
                break
            is_prime[pri*i]=False
            # i已经被筛过
            if i%pri==0:
                break
    return ans

print(prime_sleve(13))
```

:::