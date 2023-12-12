"""
Bellman-Ford 单源最短路 O(nm)
这里graph用邻接表
不过该算法一般都会被卡掉,
毕竟卡SPFA退化成Bellman-Ford都是惯例,Bellman-Ford又怎么能过呢
(特别是python)
"""

def bellman_ford(graph, src):
    """
    src: 源节点
    graph: 邻接表形式的图
    """
    V = len(graph)
    dist = [float("Inf")] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u in range(len(graph)):
            for v, w in graph[u]:
                    dist[v] =min(dist[v], dist[u] + w)
    return dist


def check_bad(graph,dist):
    """
    测试有无负权环,有则返回True
    """
    for u in range(len(graph)):
            for v, w in graph[u]:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    return True
    return False