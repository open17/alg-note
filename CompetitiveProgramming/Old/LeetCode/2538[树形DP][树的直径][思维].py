class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g=[[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        ans=0
        def f(x,fa):
            res=0
            res_lef=price[x]
            for y in g[x]:
                if y!=fa:
                    v,v_lef=f(y,x)
                    nonlocal ans
                    ans=max(ans,res+v_lef,res_lef+v)
                    res=max(res,v+price[x])
                    res_lef=max(res_lef,v_lef+price[x])
            return res,res_lef
        f(0,-1)
        return ans
        
