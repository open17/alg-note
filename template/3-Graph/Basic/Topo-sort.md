# 拓扑排序
按照入度从小到大排序的算法,也经常用于判环

通常用于解决某种先后顺序关系问题

## 模板
:::code-group


```py
"""
这里是拓扑排序的kehn算法实现
拓扑排序也经常用于判环
传入邻接边
在python3.9中可以使用graphlib实现
"""
from collections import deque

def topological_sort(in_degree,adj_list):
    sorted_nodes=[]
    queue=deque()
    for node in range(len(adj_list)):
        if in_degree[node]==0:
            queue.append(node)
    while queue:
        node=queue.popleft()
        sorted_nodes.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor]-=1
            if in_degree[neighbor]==0:
                queue.append(neighbor)
    return sorted_nodes,len(sorted_nodes)==len(in_degree)    

def get_in_degree(adj_list):
    """
    获取入度,不过这一步通常在存图的时候完成
    """
    in_degree = [0] * len(adj_list)
    for neighbors in adj_list:
        for node in neighbors:
            in_degree[node] += 1
```

:::