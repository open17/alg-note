def buildSA(s):
    n = len(s)
    x = [0] * n
    y = [0] * n
    sa = [0] * (n + 1)
    rk = [0] * (n + 1)
    m = 200
    for i in range(n):
        x[i] = ord(s[i])
        y[i] = i
    indexSort(m, sa, x, y)
    k = 1
    while k <= n and m != n:
        num = 0
        for i in range(n - k, n):
            y[num] = i
            num += 1
        for i in range(1, n + 1):
            if sa[i] >= k:
                y[num] = sa[i] - k
                num += 1
        indexSort(m, sa, x, y)
        num = 1
        x, y = y, x
        for i in range(1, n + 1):
            y1 = y[sa[i] + k] if sa[i] + k < n else 0
            y2 = y[sa[i - 1] + k] if sa[i - 1] + k < n else 0
            if i != 1 and (y[sa[i]] != y[sa[i - 1]] or y1 != y2):
                num += 1
            x[sa[i]] = num
        k *= 2
        m = num
    for i in range(1, n + 1):
        sa[i]+=1
        rk[sa[i]] = i
    return sa[1:], rk[1:]

def indexSort(m, sa, x, y):
    c = [0] * (m + 1)
    n = len(x)
    for i in range(n):
        c[x[y[i]]] += 1
    for i in range(1, m + 1):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        sa[c[x[y[i]]]] = y[i]
        c[x[y[i]]] -= 1

s = input()
sa, rk = buildSA(s)
for i in sa:
    print(i,end=" ")
print()