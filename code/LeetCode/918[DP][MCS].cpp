class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n=nums.size(),a2=-0x3f3f3f,a1=0x3f3f3f,s=0;
        int dp[n+1];
        int dp2[n+1];
        dp[0]=0;
        dp2[0]=0;
        int flag=1;
        for(int i=0;i<n;i++){
            dp[i+1]=min(dp[i],0)+nums[i];
            dp2[i+1]=max(dp2[i],0)+nums[i];
            if(dp[i+1]>=0)flag=0;
            s+=nums[i];
            a1=min(a1,dp[i+1]);
            a2=max(a2,dp2[i+1]);
        }
        if(flag)return a2;
        return max(s-a1,a2);
    }
};