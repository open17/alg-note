class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        v=[0]
        for i in nums:
            v.append(i+v[-1])
        mm=0
        ans=-inf
        for i in range(1,len(v)):
            ans=max(v[i]-mm,ans)
            mm=min(mm,v[i])
        return ans