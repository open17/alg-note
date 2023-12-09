"""
扩展欧几里得用于求出ax+by=gcd(a,b)的一组特解
通解即为 x'=x+k*b/(gcd(a,b)) y'=y-k*a/(gcd(a,b))
"""

def exgcd(a, b):
    """
    return gcd(a,b) and a pair (x,y) of func ax+by=gcd(a,b) 

    >>> exgcd(3,10)
    (1, -3, 1)
    """
    if b==0: return a,1,0
    d, x, y = exgcd(b, a % b)
    return d, y, x - (a // b) * y

if __name__ == "__main__":
    import doctest
    doctest.testmod()