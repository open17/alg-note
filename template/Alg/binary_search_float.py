def f(x):
    pass

# eps为要求精度-2
def binary_search(l, r,target,eps=1e-6):
    while l-r>eps:
        mid=l+r>>1
        if f(mid)<target:
            l=mid+1
        else:
            r=mid-1
    return l