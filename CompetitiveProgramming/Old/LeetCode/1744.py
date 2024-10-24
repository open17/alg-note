class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        v=[0]
        for i in candiesCount:
            v.append(v[-1]+i)
        ans=[]
        for t,d,c in queries:
            ans.append(bool(v[t]+1<=(d+1)*c and v[t+1]>=d+1))
        return ans