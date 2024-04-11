from bisect import bisect_left

nums=[1,3,14,28,140,999]
target=28

bisect_left(nums,target)


# 左闭右开
l,r=0,len(nums)
while l<r:
    mid=l+r>>1
    if nums[mid]<target:
        l=mid+1
    else:
        r=mid
print(l)