"""
拓扑排序 按照入度从小到大排序的算法
这里是拓扑排序的kehn算法实现
拓扑排序也经常用于判环
传入邻接边
在python3.9中可以使用graphlib实现
"""

from collections import deque

def topological_sort(in_degree,adj_list):
    # 创建一个空列表来存储排序后的节点
    sorted_nodes = []

    # 创建一个队列来存储入度为0的节点
    queue = deque()
    
    # 将入度为0的节点入队
    for node in range(len(adj_list)):
        if in_degree[node] == 0:
            queue.append(node)
    
    # 逐步移除入度为0的节点并更新相关节点的入度
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
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