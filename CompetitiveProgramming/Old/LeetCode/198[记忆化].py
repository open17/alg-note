class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def f(i):
            if i<0:
                return 0
            return max(f(i-1),f(i-2)+nums[i])
        return f(len(nums)-1)
