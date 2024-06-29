import random
import time


random.seed(int(time.time()))

f=["A","C","T","G","*","?"]

s=""
for i in range(random.randint(1, 5)):
    s+=random.choice(f)

print(s)

f=f[:-2]
m=random.randint(1, 5)
print(m)
for _ in range(m):
    n=random.randint(1, 10)
    s=""
    for _ in range(n):
        s+=random.choice(f)
    print(s)

