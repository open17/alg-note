# 倍增
它能够使得线性的处理转化为对数级的处理，大大地优化时间复杂度[^1]



与其说倍增是算法,不如说它是一种思想,它能够帮助我们优化算法



## 倍增优化查找

一般这种题目也能转化为二分

相较于二分来说对于小区间(答案可能比较小的时候)常数更好一些

或者二分不知道上界的时候,可能使用倍增会好一些

## 倍增优化转移
选择 $1,2,4,...,2^i$ 我们可以通过加减表示出区间 $[1,2^{i+1})$  
所以我们只需要记录 $floor(log_2n)$ 个状态就可以计算n个状态

本质: $2^i=2^{i-1}+2^{i-1}$ 效率比 $2^i=(2^i-1)+1$ 转移要高

也就是说,问题存在自乘关系时,我们便可以利用倍增来优化

通常我们会使用 $f(i,p)=f(f(i,p-1),p-1)$ 进行倍增转移, $i$ 表示当前点, $p$ 表示当前点跳 $2^p$ 步

## 运用
> 下面是一些倍增的经典模板

### 快速幂取模
```py
def qpow(a,b,p):
    ans=1
    while b:
        if b&1:
            ans=(ans*a)%p
        a=(a*a)%p
        b>>=1
    return ans
```
### 矩阵快速幂
重点在于把数列转为矩阵幂
方法列出ax+ax-1+...转为A*(ax-1+ax-2+...)然后就变为A*A*...*(base step)
```py
def matrix_multiply(A, B,mod):
    rows_A,cols_A,cols_B=len(A),len(A[0]),len(B[0])
    res=[[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                res[i][j]+=(A[i][k]*B[k][j])%mod
                res[i][j]%=mod
    return res

def matrix_power(matrix, n,mod=int(1e9+7)):
    rows, cols=len(matrix), len(matrix[0])
    result=[[1 if i==j else 0 for j in range(cols)] for i in range(rows)]
    while n:
        if n%2:
            result=matrix_multiply(result, matrix,mod)
        matrix=matrix_multiply(matrix, matrix,mod)
        n//=2
    return result

# 示例使用
matrix = [[1, 1], [1, 0]]  # 斐波那契数列的矩阵形式
n = 5  # 计算第5个斐波那契数
result = matrix_power(matrix, n)
fibonacci_number = result[0][1]  # 结果矩阵的第一行第二列即为斐波那契数
print(fibonacci_number)
```
### ST表
### 树上倍增-LCA










[^1]: 摘自[【朝夕的ACM笔记】算法基础-倍增](https://zhuanlan.zhihu.com/p/122413160)
