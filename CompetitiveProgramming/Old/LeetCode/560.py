class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        v=[0]
        for i in nums:
            v.append(v[-1]+i)
        d=defaultdict(int)
        cnt=0
        for i in v:
            cnt+=d[i]
            d[k+i]+=1
        return cnt
            