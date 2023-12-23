"""
扩展欧几里得用于求出ax+by=gcd(a,b)的一组特解
通解即为 x'=x+k*b/(gcd(a,b)) y'=y-k*a/(gcd(a,b))

同时显然知道扩展欧几里得后,裴蜀定理的正确性自然一目了然

>>> exgcd(3,10)
    (1, -3, 1)
"""

def exgcd(a, b):
    if b==0: return a,1,0
    d, x, y = exgcd(b, a % b)
    return d, y, x - (a // b) * y

if __name__ == "__main__":
    import doctest
    doctest.testmod()