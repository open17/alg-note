class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        int dp[n+5];
        memset(dp,0,sizeof(dp));
        for(int i=2;i<n+2;i++){
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-2]);
        }
        return dp[n+1];
    }
};