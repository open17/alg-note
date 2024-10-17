class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c={}
        a=[]
        for i in nums:
            if i not in c.keys():
                c[i]=1
                a.append(i)
            else:
                c[i]+=1
        a.sort()

        # @cache
        # def f(i):
        #     if i<0:
        #         return 0
        #     if i==0:
        #         return a[0]*c[a[0]]
        #     ans=f(i-1)
        #     if a[i]==a[i-1]+1:
        #         ans=max(ans,f(i-2)+a[i]*c[a[i]])
        #     else:
        #         ans=max(ans,f(i-1)+a[i]*c[a[i]])
        #     return ans
        # # print(a,f(2))
        # return f(len(a)-1)

        f=[0]*len(a)
        f[0]=a[0]*c[a[0]]

        for i in range(1,len(a)):
            ans=f[i-1]
            if a[i]==a[i-1]+1:
                if i-2>=0:
                    ans=max(ans,f[i-2]+a[i]*c[a[i]])
                else:
                    ans=max(ans,a[i]*c[a[i]])
            else:
                ans=max(ans,f[i-1]+a[i]*c[a[i]])
            f[i]=ans
        return f[-1]
        
            