# 字符串哈希

## 什么是?

定义多项式 Hash 函数：

$$f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$$


## 模板

双模数,可能慢一些,但不容易被卡

:::code-group

<<< @/../template/String/hash.py

:::

## 例题

幽默一刻:![被卡掉](https://cdn.jsdelivr.net/gh/open17/Pic/img/202404121358256.png)

单随机模数和BASE中奖,给测试用例卡掉了,再提交一遍不改代码就过了

<<< @/../code/LeetCode/3031[哈希二分].py