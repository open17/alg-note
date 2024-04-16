# 最短路

## 堆优化Dijkstra算法
- 时间$O(mlogm)$ 
- 原理: 贪心操作取距离顶点最近且没有被访问过的点松弛
- 所以无法处理负权
:::code-group

<<< @/../template/Graph/dijkstra.py

:::

## SPFA
- 队列优化的bellman-ford,去掉无用的松弛操作
- 但依然可能被卡成bellman-ford
- 判负权环:
    - 用数组记录顶点进队的次数
    - 当一个顶点进队超过n次时,存在负权环
:::code-group

<<< @/../template/Graph/SPFA.py

:::

## 弗洛伊德
- 允许负权，不允许负环
- 多源最短
- 立方复杂度
:::code-group

<<< @/../template/Graph/floyd.py

:::