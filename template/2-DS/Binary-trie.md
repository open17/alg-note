# 01字典树

## 什么是?
用于解决一些异或问题,也可以用于模拟平衡树(但是我不会)

譬如对求一组数和x的最大异或值

## 策略
如果我们要找与给定数异或最大的数，就尽可能走与该数当前位不同的路径
反之则尽可能走与当前位相同的路径

值得注意的是应该从最高位开始走,这是个要注意的贪心的点,因为最高位贡献大

## 标准模板

:::code-group

```cpp
int nxt[(int)5e6+1][2];
int cnt=0;
void insert(int v){
    int cur=0;
    for(int i=30;i>=0;i--){
        int p=(v>>i)&1;
        if(!nxt[cur][p])nxt[cur][p]=++cnt;
        cur=nxt[cur][p];
    }
}
int get(int v){
    int cur=0,val=0;
    for(int i=30;i>=0;i--){
        int p=(v>>i)&1;
        if(nxt[cur][p^1]){
            cur=nxt[cur][p^1];
            val+=1<<i;
            continue;
        }
        cur=nxt[cur][p];
    }
    return val;
}
```

```py
MAXBIT = 31

nxt = [[0,0]]
num = {}
global cnt
cnt=1
def insert(n):
    global cnt
    cur = 1
    for i in range(MAXBIT, -1, -1):
        bit = (n >> i) & 1
        while cur+1>=len(nxt):
            nxt.append([0,0])
        if not nxt[cur][bit]:
            cnt += 1
            nxt[cur][bit] = cnt
        cur = nxt[cur][bit]
    num[cur] = n
def find_max(x):
    cur = 1
    for i in range(MAXBIT, -1, -1):
        bit = (x >> i) & 1
        if nxt[cur][bit ^ 1]:
            cur = nxt[cur][bit ^ 1]
        else:
            cur = nxt[cur][bit]
    return x ^ num[cur]
```

:::

## 可撤销模板

```cpp
int nxt[(int)3e5+10][2][2];
int cnt=0;
void insert(int v){
    int cur=0;
    for(int i=30;i>=0;i--){
        int p=(v>>i)&1;
        if(!nxt[cur][p][0])nxt[cur][p][0]=++cnt;
        nxt[cur][p][1]++;
        cur=nxt[cur][p][0];
    }
}
void del(int v){
    int cur=0;
    for(int i=30;i>=0;i--){
        int p=(v>>i)&1;
        nxt[cur][p][1]--;
        cur=nxt[cur][p][0];
    }
}
int get(int v){
    int cur=0,val=0;
    for(int i=30;i>=0;i--){
        int p=(v>>i)&1;
        if(nxt[cur][p^1][1]>0){
            cur=nxt[cur][p^1][0];
            val+=1<<i;
            continue;
        }
        cur=nxt[cur][p][0];
    }
    return val;
}
```
