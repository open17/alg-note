from collections import deque

def spfa(graph, src):
    """
    src: 源节点
    graph: 邻接表形式的图
    """
    V = len(graph)
    dist = [float("Inf")] * V
    dist[src] = 0

    queue = deque()
    queue.append(src)
    in_queue = [0] * V
    in_queue[src] = 1

    while queue:
        u = queue.popleft()
        in_queue[u] = 0
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = 1
    return dist