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