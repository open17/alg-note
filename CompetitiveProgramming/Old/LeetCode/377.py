class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # @cache
        # def f(i):
        #     if i<=0:
        #         return int(i==0)
        #     ret=0
        #     for j in nums:
        #         ret+=f(i-j)
        #     return ret
        # return f(target)
        f=[0]*(target+1)
        f[0]=1
        for i in range(target+1):
            for v in nums:
                if i<v: continue
                f[i]+=f[i-v]
        return f[-1]