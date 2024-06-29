# 卡常

## c++

### 引用快于新建

`map<int,stl>`的时候stl要引用,否则常数很大

### vector?

有时候vector会被幽默卡常,现在我一般喜欢直接动态(g++)分配数组或开全局

### define long long

其实常数还是挺大的,卡的时候可以去掉,注意加法乘法取模前也可能溢出要转类型即可

## python

### 初始化优化

cpython中推导式初始化比for循环快


### 插入优化

```py
>>> a=[1,3,4,5]
>>> i=1
>>> v=2
>>> a[i:i]=[v]
```

a[i:i] = [v] 的底层实现,其中i为要插入的位置,v为值:
调用c的memmove 库函数来搬运插入之后的元素,
快于insert


### __slot__优化

python的class一般都比较慢,可以加入__slot__来优化

### array优化

使用array替代list,注意array是定内容类型的,比如指定只能int

### 极限cache

可以clear也可以del函数(在leecode这种同一调用的情况下比价有用)