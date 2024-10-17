class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        f(i)=min(f(i-1),f(i-2))+cost[i]
        """
        cost.append(0)
        f=[0]*(len(cost)+2)
        for i,v in enumerate(cost):
            f[i+2]=min(f[i+1],f[i])+cost[i]
        return f[-1]
