class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        p=[]
        while n:
            ans=n&(-n)
            n-=ans
            p.append(int(log2(ans)))
        a=[0]
        for i in p:
            a.append(a[-1]+i)
        ans=[]
        for l,r in queries:
            ans.append(pow(2,a[r+1]-a[l],10**9+7))
        return ans