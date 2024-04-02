n=20
s=6

# 遍历集合
for i in range(n):
    if (s >> i) & 1:
        pass
# 枚举[0,n-1]全部集合
for s in range(1 << n):
    pass
# 枚举s的非空子集
sub = s
while sub:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s

# 从大到小枚举 s 的所有子集(s到空)
sub = s
while True:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s
    if sub == s:
        break