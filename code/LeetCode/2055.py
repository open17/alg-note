class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # back
        a=[-1]*len(s)
        # front
        b=[-1]*len(s)
        v=[0]
        pa=0
        pb=len(s)-1
        for idx,c in enumerate(s):
            p=1
            if c=="|":
                for j in range(pa,idx+1):
                    a[j]=idx
                pa=idx+1
                p=0
            v.append(v[-1]+p)    
        for i in range(len(s)-1,-1,-1):
            if s[i]=="|":
                for j in range(pb,i-1,-1):
                    b[j]=i
                pb=i-1
        ans=[]
        for l,r in queries:
            l=a[l]
            r=b[r]
            if l==-1 or r==-1 or l>r:
                ans.append(0)
                continue
            ans.append(v[r+1]-v[l])
        return  ans
            

