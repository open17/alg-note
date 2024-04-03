def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a**(1/2)) + 1):
        if a % i == 0:
            return False
    return True