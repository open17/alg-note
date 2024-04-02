def exgcd(a, b):
    if b==0: return a,1,0
    d, x, y = exgcd(b, a % b)
    return d, y, x - (a // b) * y