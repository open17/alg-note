# ST表
```py
import math

def init_st(arr):
    n=len(arr)
    logn=int(math.log2(n+1)) + 1
    st=[[0] * logn for _ in range(n+1)]
    for i in range(1, n+1):
        st[i][0]=arr[i]
    for j in range(1, logn):
        for i in range(1, n+1):
            if i+(1<<j)-1<=n:
                st[i][j]=min(st[i][j-1],st[i+(1<<(j-1))][j-1])
    return st

def query_st(st, left, right):
    length=right-left+1
    k=int(math.log2(length))
    return min(st[left][k], st[right-(1<<k)+1][k])

# 示例使用
arr = [4, 2, 5, 1, 3, 6, 8, 7]
st_table = build_st_table(arr)

# 查询区间 [2, 6] 的最小值
left = 2
right = 6
result = query_st_table(st_table, left+1, right+1)
print(result)
```