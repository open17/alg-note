"""

先枚举出2的幂,而不是枚举n的组合

"""
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def getlen(x):
            cnt=0
            while x:
                x//=10
                cnt+=1
            return cnt
        def getcnt(x):
            ans=[0 for _ in range(10)]
            while x:
                ans[int(x%10)]+=1
                x//=10
            return ans
        tol_n=getlen(n)
        cnt_n=getcnt(n)
        # print(cnt_n)
        x=1
        flag=0
        while x<=1e9:
            if getlen(x)==tol_n:
                tmp=getcnt(x)
                for i,j in zip(tmp,cnt_n):
                    if i!=j:
                        break
                else:
                    flag=1
                    break
            if getlen(x)>tol_n:
                break
            x*=2
        return bool(flag)
         