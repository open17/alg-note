class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        child=3
        @cache
        def f(i,n):
            if i>=child-1:
                return int(n<=limit)
            ans=0
            for k in range(min(n,limit)+1):
                ans+=f(i+1,n-k)
            return ans
        return f(0,n)