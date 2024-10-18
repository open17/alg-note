class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(a):
            # f(x)=max(f(x-1),f(x-2)+a[x])
            if len(a)==0:
                return 0
            x,y=0,0
            for i in a:
                x,y=max(x,y+i),x
            return x
        return max(rob1(nums[2:-1])+nums[0],rob1(nums[1:]))