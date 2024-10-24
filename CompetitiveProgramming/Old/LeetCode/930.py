class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        v=[0]
        for i in nums:
            v.append(v[-1]+i)
        d=defaultdict(int)
        cnt=0
        # r-i=goal
        for i in v:
            cnt+=d[i]
            d[goal+i]+=1
        return cnt