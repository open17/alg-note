# 树的直径

一棵树的直径指的是树中任意两个节点之间的最长路径长度。

## 思路

树形DP,本质是枚举拐点

有时候DP计算边好写,有时候计算点好写,只需要记住边与点的转换关系即可(边+1=点,注意特殊情况点/边为0要特别处理)

## 代码

```py
ans=0
def f(root,fa):
    res=0
    for son in g[root]:
        if son==fa: continue
        v=f(son,root)+1
        global ans
        ans=max(ans,v+res)
        res=max(res,v)
    return res
```

## 更多

- [树形DP-树的直径学习笔记](https://www.open17.vip/posts/xcpc/2024-04-12-%E6%A0%91%E7%9A%84%E7%9B%B4%E5%BE%84.html)
