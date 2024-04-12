class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=int(1e9)+7

        # f(i)=f(i-zero)+f(i-one)
        # @cache
        # def f(i):
        #     if i<=0:
        #         return int(i==0)
        #     return (f(i-zero)%MOD+f(i-one)%MOD)%MOD
        # s=0
        # for i in range(low,high+1):
        #     s+=f(i)%MOD
        #     s%=MOD
        # return s

        f=[0]*(high+1)
        f[0]=1
        res=0
        for i in range(1,high+1):
            ans=0
            if i-zero>=0:
                ans+=f[i-zero]%MOD
                ans%=MOD
            if i-one>=0:
                ans+=f[i-one]%MOD
                ans%=MOD
            f[i]=ans
            if i>=low:
                res+=f[i]%MOD
                res%=MOD
        return res



