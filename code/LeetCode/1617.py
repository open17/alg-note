class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n+5)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        res=[0 for _ in range(n)]
        use=ans=0
        def f(x,p):
            ret=0
            for y in g[x]:
                nonlocal use,ans
                if (not (p>>(y-1))&1) or (use>>(y-1))&1:
                    continue
                use|=1<<(y-1)
                length=f(y,p)
                length+=1
                ans=max(ans,ret+length)
                ret=max(ret,length)
            return ret
        for p in range(1,1<<n):
            use=p&(-p)
            ans=0
            root=int(log2(p&(-p)))+1
            f(root,p)
            if use==p:
                res[ans]+=1
        return res[1:]