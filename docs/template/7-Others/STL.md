# STL  

基本数据结构的STL  

::: tip 🤖内容生成预警
由于我很懒,该部分内容使用AI生成,请谨慎鉴别
:::
## 数组

:::code-group

```cpp
vector<int> a(size,val);
*a.begin()==a.front();
*a.end()==a.back();
a.empty();
a.size();
a.clear();
a.push_back(1);
a.pop_back();
```

```py
a=[i for i in range(10)]
print(a[0],a[-1])
a.append(10)
print(a)
a.pop()
print(a)
```

:::

## 栈
:::code-group

```cpp
stack<int> s;
s.push(1);
s.top();
s.pop();
s.empty();
s.size();

```

```py

```

:::
## 队列
:::code-group

```cpp
queue<int> q;
q.push(1);
q.front();
q.back();
q.pop();
q.empty();
q.size();

```

```py

```

:::
## 双端队列
:::code-group

```cpp
deque<int> dq;
dq.push_back(1);
dq.push_front(2);
dq.pop_back();
dq.pop_front();
dq.front();
dq.back();
dq.empty();
dq.size();

```

```py
from collections import deque

dq = deque([i for i in range(10)])
print(dq[0], dq[-1])
dq.append(10)
print(dq)
dq.pop()
print(dq)

```

:::
## 堆
:::code-group

```cpp
priority_queue<int> pq;
pq.push(1);
pq.top();
pq.pop();
pq.empty();
pq.size();

```

```py
h=heapify([1,2,3])
heappush(h,1)
y=heappop(h)
```

:::
## 哈希表
:::code-group

```cpp
unordered_map<int, int> mp;
mp.insert({1, 10});
mp[1];
mp.erase(1);
mp.empty();
mp.size();
```

```py
a={}
a=defaultdict(lambda x:[1,2,3])
```

:::
## 集合
:::code-group

```cpp
unordered_set<int> st;
st.insert(1);
st.erase(1);
st.empty();
st.size();

```

```py
a=set()
a.add(1)
```

:::
## 排序
:::code-group

```cpp
sort(arr, arr + n);
sort(a.begin(), a.end());

```

```py
a.sort()
sorted(a,key=lambda x:x[1])
```

:::
