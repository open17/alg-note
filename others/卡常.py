"""
python 卡常技巧


初始化优化
python中推导式初始化比for循环快

>>> a=[1,3,4,5]
>>> i=1
>>> v=2
>>> a[i:i]=[v]


插入优化
a[i:i] = [v] 的底层实现,其中i为要插入的位置,v为值:
调用c的memmove 库函数来搬运插入之后的元素,
快于insert


__slot__优化
python的class一般都比较慢,可以加入__slot__来优化



"""



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)