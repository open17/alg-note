"""

g为邻接表

"""

ans=0
def f(root):
    res=0
    for son in g[root]:
        v=f(son)+1
        global ans
        ans=max(ans,v+res)
        res=max(res,v)
    return res