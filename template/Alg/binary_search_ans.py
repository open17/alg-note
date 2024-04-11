def check(val):
    pass
# 假设左闭右开,要找到最后一个满足条件的值,越大越容易不满足时
def binary_search(l,r):
    while l<r:
        mid=l+r>>1
        if check(mid):
            l=mid+1
        else:
            r=mid
    return l-1