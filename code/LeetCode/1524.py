class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD=10**9+7
        v=[0]
        for i in arr:
            v.append(i+v[-1])
        # 奇奇为偶,偶偶为偶,奇偶为奇
        even=0
        odd=0
        cnt=0
        for i in v:
            # 奇
            if i&1:
                odd+=1
                even%=MOD
                cnt+=even
            else:
                even+=1
                odd%=MOD
                cnt+=odd
            cnt%=MOD
        return cnt


                