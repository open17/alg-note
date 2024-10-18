class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // dp[i]=dp[i-1]+nums[i]
        int n=nums.size();
        int dp[n+1];
        dp[0]=0;
        int ans=-0x3f3f3f;
        for(int i=0;i<n;i++){
            dp[i+1]=nums[i];
            if(dp[i]>0)dp[i+1]+=dp[i];
            ans=max(ans,dp[i+1]);
        }   
        return ans;
    }
};