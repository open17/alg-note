# 语法糖
## python
### zip
下面两个是等价的
```py
c=list(zip(a,b))

c=[(a[i],b[i]) for i in range(min(len(a),len(b)))]
```
注意python3中zip返回的是迭代器,如果需要转为数组请用list
### enumerate
获取下标和值
```py
a=[5,2,0]
for idx,i in enumerate(a):
    print(idx,i)
# 输出
# 0 5
# 1 2
# 2 0
```
### cache
@cache,为函数参数与返回值建立缓存,避免重复计算
通常用于记忆化
### 海象运算符
`(a:=b)`先赋值,再判断
即先给a赋值b,然后外面判断a的性质
比如下面两个是等价的
```py
a=5
if a>4:
    print(a)

if (a:=5)>4:
    print(a)
```
### reduce
返回函数计算的结果
```py
reduce(function, iterable[, initial])
```
### `__slot__`
在python中,类支持动态加载属性,这个时候会开一个哈希,耗时较多
但通常ACM中数据结构不需要动态加载属性,所以可以使用__slot__来限制类只能加载__slot__中定义的属性,从而提高运行速度
```py
self.__slot__ = ['a', 'b']
```
### permutations 与 combinations
k表示选几个,a为数组
`combinations(a: list,k: int)`: 组合,返回迭代器
`permutations(a: list,k: int)`: 排列,返回迭代器
### defaultdict
`defaultdict(type)`,有默认值的字典
### Counter
`Counter(a)`,统计元素个数,类似哈希表的用法
### lambda
匿名函数,常见于`sorted`,`reduce`等
格式:`lambda x:...`,`lambda x,y:...`
### for else
```py
for `临时变量` in `序列`:
    `重复执行的代码`
    ......
else:
    `循环中途没有break正常结束时执行的代码`
```
### 推导式
`[x for x in a]`: 列表推导式