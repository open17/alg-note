# 懒删除

## 什么是?

懒删除是一种非常常见的思想

当需要多次删除/替换堆中元素(不保证最小/最大),且查询操作与该操作是分离的时候,我们可以对要处理的元素打上懒标记,在查询的时候再调整堆

::: details 例题

[LC数字容器系统](https://leetcode.cn/problems/design-a-number-container-system/description/)

设计一个数字容器系统，可以实现以下功能：

- 在系统中给定下标处 插入 或者 替换 一个数字。
- 返回 系统中给定数字的最小下标。

这题是非常明显的懒删除堆,当然也可以平衡树

```cpp
class NumberContainers {
    map<int,int> a;
    map<int,priority_queue<int, vector<int>>>b; 
public:
    NumberContainers() {

    }
    
    void change(int index, int number) {
        a[index]=number;
        b[number].push(-index);
    }
    
    int find(int number) {
        if(!b.count(number))return -1;
        // 下面会超时
        // priority_queue<int, vector<int>> q =b[number];
        auto &q=b[number];
        while(!q.empty()&&(a[-q.top()]!=number)){
            q.pop();
        }
        return q.empty()?-1:-q.top();
    }
};
```
:::