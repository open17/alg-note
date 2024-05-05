class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        n=len(frame)
        m=len(frame[0])
        # @lru_cache(maxsize=None)
        # def f(i,j):
        #     if i>=n or j>=m:
        #         return 0
        #     return max(f(i+1,j),f(i,j+1))+frame[i][j]
        # return f(0,0)

        f=deepcopy(frame)
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                elif i==0:
                    f[i][j]+=f[i][j-1]
                elif j==0:
                    f[i][j]+=f[i-1][j]
                else:
                    f[i][j]+=max(f[i-1][j],f[i][j-1])
        return f[-1][-1]