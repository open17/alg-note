# 扩展欧几里得

性质: 若$ax+by=d$,则有$d=gcd(a,b)$

可视为裴蜀定理的逆定理

:::code-group

```py
def exgcd(a, b):
    if b==0: return a,1,0
    d, x, y = exgcd(b, a % b)
    return d, y, x - (a // b) * y
```
:::