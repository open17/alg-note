# 对顶堆

## 什么是?
用于动态维护第k大/第k小


## 实现

这里维护第k大(维护第k小对元素取负即可)
- 建立一大一小两个堆
- 记住小维护大,大维护小
- 小根堆用于维护值前k大的元素
- 大根堆用于维护值小于k大的元素
- 维护,一个堆超大小了就取出来丢到另外一个堆即可
- 插入的话,小于小根堆堆顶的元素就丢到大根堆,否则相反,然后维护
- 记得python中大根堆都是相反数
- 记得每次插入完都要update一下,有些题目会改变k,所以就不写死了insert后调用update

## 模板

:::code-group

```py
from heapq import heapify,heappush,heappop
lo_heap=[]
hi_heap=[]
def insert(x):
    if not lo_heap or x>=lo_heap[0]:
        heappush(lo_heap,x)
    else:
        heappush(hi_heap,-x)

def find():
    return lo_heap[0]

def update(k):
    size=len(hi_heap)+len(lo_heap)
    if k>size:
        return
    while len(lo_heap)<k:
        if hi_heap: 
            heappush(lo_heap,-heappop(hi_heap))
        else: 
            break
    while len(hi_heap)<size-k:
        heappush(hi_heap,-heappop(lo_heap))
        
```

:::
