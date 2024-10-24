class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int dp[high+5];
        dp[0]=1;
        int ans=0;
        int MOD=1e9+7;
        for(int i=1;i<=high;i++){
            dp[i]=0;
            if(i>=zero)dp[i]=(dp[i]+dp[i-zero])%MOD;
            if(i>=one)dp[i]=(dp[i]+dp[i-one])%MOD;
            if(i>=low&&i<=high)ans=(ans+dp[i])%MOD;
        }
        return ans;
    }
};