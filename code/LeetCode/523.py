class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        v=[0]
        for i in nums:
            v.append(v[-1]+i)
            v[-1]%=k
        d=defaultdict(lambda :-1)
        for idx,i in enumerate(v):
            if d[i]==-1:
                d[i]=idx
            elif idx-d[i]+1>2:
                    return True
        return False
