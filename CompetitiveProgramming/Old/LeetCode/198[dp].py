class Solution:
    def rob(self, nums: List[int]) -> int:
        f=[0]*(len(nums)+2)
        for i,v in enumerate(nums):
            f[i+2]=max(f[i+1],f[i]+v)
        return f[-1]
