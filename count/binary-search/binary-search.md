# 二分

## 基础二分
```py
bisect_left(nums,target)

# 左闭右开
while l<r:
    mid=l+r>>1
    if a[mid]<target:
        l=mid+1
    else:
        r=mid
return l
```
## 二分答案
> 解题的时候往往会考虑枚举答案然后检验枚举的值是否正确。若满足单调性，则满足使用二分法的条件。把这里的枚举换成二分，就变成了「二分答案」  --OI WIKI

事实上不需要单调性,题目条件满足二段性即可尝试二分答案

注意事项:
- 注意二分的边界,有时候题目在某段边界才满足二段性,所以左指针右指针不要无脑0和inf
  
```py
def check(val):
    pass
# 假设左闭右开,要找到最后一个满足条件的值,越大越容易不满足时
while l<r:
    mid=l+r>>1
    if check(mid):
        l=mid+1
    else:
        r=mid
return l-1
```


## 浮点二分
浮点二分不用考虑开闭,一般精度比题目要求的小两个数量级即可
```py
def f(x):
    pass

eps=1e6

while l-r>eps:
    mid=l+r>>1
    if f(mid)<target:
        l=mid+1
    else:
        r=mid-1
return l
```



