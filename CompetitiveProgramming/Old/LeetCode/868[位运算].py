class Solution:
    def binaryGap(self, n: int) -> int:
        idx,ans=inf,0
        while n:
            tmp=int(log2(n&-n))
            idx,ans=tmp,max(ans,tmp-idx)
            n&=(n-1)
        return ans