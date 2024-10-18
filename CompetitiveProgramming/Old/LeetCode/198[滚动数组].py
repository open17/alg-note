class Solution:
    def rob(self, nums: List[int]) -> int:
        a=b=0
        for i,v in enumerate(nums):
            c=max(b,a+v)
            a=b
            b=c
        return b
