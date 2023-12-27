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

p=[8,10,23,2,4,91,1,1,77,332,1]

for i in p:
    insert(i) 
    update(3) 
    print(find())
    