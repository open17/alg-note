class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n=len(edges1)
        m=len(edges2)
        g1=[[] for _ in range(n+1)]
        g2=[[] for _ in range(m+1)]
        for a,b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a,b in edges2:
            g2[a].append(b)
            g2[b].append(a)
        
        def f(root,fa,g):
            res=0
            ans=0
            for son in g[root]:
                if son==fa:
                    continue
                v,pv=f(son,root,g)
                v+=1
                ans=max(ans,v+res,pv)
                res=max(res,v)
            return res,ans
        
        a=f(0,-1,g1)[1]
        b=f(0,-1,g2)[1]
        return max(a,b,(a+1)//2+(b+1)//2+1)
        