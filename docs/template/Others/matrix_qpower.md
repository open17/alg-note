# 矩阵快速幂

## 什么是?

矩阵快速幂,即使用快速幂的方法处理矩阵的幂,两者本质上是一样的,只需把常数乘法转为矩阵乘法即可

## 如何用?

什么时候需要使用矩阵的快速幂? 一般可用于对于递推公式的加速

以斐波那契数列为例, 递推公式为: $f(n) = f(n-1) + f(n-2)$,同时满足条件$f(1)=f(2)=1$,求$f(n)$

:::warning 注意
矩阵乘法不满足交换律,别写错了  

构造右边的结果矩阵是几维?  当然看递推公式和base
:::

构造矩阵表述:

$$
\begin{bmatrix}
1 & 1\\
1 & 0 \\
\end{bmatrix}
\times
\begin{bmatrix}
F_{n-1} \\
F_{n-2} \\
\end{bmatrix}
{=}
\begin{bmatrix}
F_n \\
F_{n-1} \\
\end{bmatrix}
$$

递推得:

$$
\begin{bmatrix}
1 & 1\\
1 & 0 \\
\end{bmatrix}^{n-3}
\times
\begin{bmatrix}
F_{1} \\
F_{2} \\
\end{bmatrix}
{=}
\begin{bmatrix}
F_n \\
F_{n-1} \\
\end{bmatrix}
$$

因为$F_1,F_2$已知,只需求出左边矩阵的幂即可求出$F_n$

因此利用快速矩阵幂即可加速递推的求解



## 模板

:::code-group

<<< @/../template/Others/matrix_qpower.py

:::