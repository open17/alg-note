# 二叉堆
## 小根堆
python内置小根堆,等价大根堆对元素取负即可
```py
from heapq import heapify,heappush,heappop
a=[1,2,3,4,5,6,7,8,9]
heapify(a)
heappush(a,10)
heappop(a)
```
