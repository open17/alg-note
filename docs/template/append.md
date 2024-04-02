# 附录

## python常见问题
### 除法
在python中`/`是浮点除法,整除是`//`
### 深拷贝
python中对于可变对象一般都是浅拷贝(复制指针)
很多时候对数组我们需要深拷贝,通常方法如下
- `deepcopy(a)`
- `a[::]`
### 字典序
python的str可以直接比较字典序
### 浮点高精度
在python中浮点数的精度是有限的
我们可以通过导入decimal库来实现浮点高精,其中高精度数用字符串传入
```py
from decimal import Decimal, getcontext
# 精度范围
getcontext().prec = 20
a=Decimal('6.0000003')
```
### 负数取余
python负数取余为正数,无需处理