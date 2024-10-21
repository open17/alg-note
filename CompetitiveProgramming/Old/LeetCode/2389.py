class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        a=[0]
        for i in nums:
            a.append(a[-1]+i)
        ans=[]
        for q in queries:
            ret=bisect_left(a,q+1)-1
            ans.append(ret)
        return ans    
