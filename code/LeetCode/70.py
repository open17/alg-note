class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def f(i):
        #     if i==0:
        #         return 1
        #     if i<0:
        #         return 0
        #     return f(i-1)+f(i-2)
        # return f(n)

        #  转移  f(i+2)=f(i+1)+f(i)
        
        # f=[0]*(n+2)
        # f[1]=1
        # for i in range(n):
        #     f[i+2]=f[i+1]+f[i]
        # return f[-1]

        a,b=0,1
        for i in range(n):
            c=a+b
            a=b
            b=c
        return b


