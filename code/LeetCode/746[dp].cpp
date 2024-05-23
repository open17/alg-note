class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // f[i]=min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])
        int n=cost.size();
        int f[n+2];
        memset(f,0,sizeof(f));
        for(int i=0;i<n-1;i++){
            f[i+2]=min(f[i+1]+cost[i+1],f[i]+cost[i]);
            // cout<<f[i+2]<<endl;
        }
        return f[n];
    }
};