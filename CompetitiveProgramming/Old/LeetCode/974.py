class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        v=[0]
        for i in nums:
            v.append(v[-1]+i%k)
            v[-1]%=k
        # l%k-r%k==0
        d=defaultdict(int)
        cnt=0
        for i in v:
            cnt+=d[i]
            d[i]+=1
        return cnt         