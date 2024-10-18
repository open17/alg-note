class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n=len(parent)
        g=[[] for _ in range(n)]
        for i in range(1,n):
            g[parent[i]].append(i)
        ans=0
        def f(root):
            if root>=n:
                return 0
            res=0
            for son in g[root]:
                v=f(son)+1
                nonlocal ans
                if s[root]!=s[son]:
                    ans=max(ans,v+res)
                    res=max(res,v)
            return res
        f(0)
        return ans+1