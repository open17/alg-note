class Solution:
    def countHousePlacements(self, n: int) -> int:
        # f[i]=f[i-1]+1+f[i-2]
        MOD=10**9+7
        f=[0]*(n+2)
        for i in range(n):
            f[i+2]=(f[i+1]%MOD+1+f[i]%MOD)%MOD
        return ((f[-1]+1)**2)%MOD