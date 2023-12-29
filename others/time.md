# 时间复杂度分析
> Worst-Case Cost is the focus of our analysis
## basic operations
要注意+=操作的basic operations是2
```cpp
a+=1
```
一个for循环的复杂度
```cpp
// 1 + (n+1)*1 + n*2 = 3n+2
for(int i = 0; i < n; i++ [i += 1])
```
看看下面的basic operations?
```cpp
int afunc (int n) {
    int res = 0; // 1
    for(int i = 0; i < n; i++) // 1 + (n+1)*1 + n*2 = 3n+2
        for(int j = 1; j < n; j*=2) // [1 + (log(n) +1)*1 + log(n)*2]*n = [3log(n) +2]*n
            res += i * j; // {[1 + 1 + 1]*log(n)}*n = 3log(n)*n
    return res; // 1
}
```
$T(n) = 1+(3n+2) + (3log(n)+2)*n + 3log(n)*n + 1 = 6nlog(n) + 5n + 4$

## 时间复杂度
### Big-O: The Upper Bound
$f(n) = O(g(n))$
Definition: There are positive constants $c$ and $n_0$ such that 
$f(n)<=c*g(n) \text{, when } n >= n_0$

### Big-Omega: The Lower Bound
f(n) = $\Omega(g(n))$

### Big-Theta: Tight Bound
f(n) = $\Theta(g(n))$=$\Omega(g(n))$=$O(g(n))$

## 辅助分析工具
### 常见增长率
![](https://cdn.jsdelivr.net/gh/open17/Pic/img/202311071518182.png)



### 数学
> 在复杂度分析时我们很可能要用到一些数学知识来帮助分析

#### 数学基础回顾
![](https://cdn.jsdelivr.net/gh/open17/Pic/img/202311071518183.png)

#### L' Hopital's rule
$\lim_{n\rightarrow\infty}\frac{f(n)}{g(n)}=\lim_{n\rightarrow\infty}\frac{f(n)'}{g(n)'}$

#### 重要结论
if 0:	$f(N)$ $=$ $O(g(N))$ and $f(N)$ is not $\Omega(g(n))$
if constant:	$f(N)$ $=$  $\Theta(g(n))$
if  $\infty$   $f(N)$ $=$ $\Omega(g(n))$ and $f(N)$ is not $O(g(N))$
limit oscillates:	no relation

### General Rules
#### General Rules1
嵌套相乘(如两个for嵌套循环,注意两个循环应独立)
#### General Rules 2
非嵌套相加取最大
#### General Rules 3
计算递归函数的复杂度示例:
```cpp
int sum(int n) {
    if(n<=0)
        return 0;
    return n + sum(n-1);
}
```
![](https://cdn.jsdelivr.net/gh/open17/Pic/img/202311071518186.png)
![](https://cdn.jsdelivr.net/gh/open17/Pic/img/202311071518185.png)
