class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        long long n=arr.size()*min(k,2),ans=0,s=0,MOD=1e9+7;
        long long dp[n+1];
        dp[0]=0;
        for(int i=0;i<n;i++){
            dp[i+1]=(max(dp[i],0LL)+arr[i%arr.size()]);
            ans=max(ans,dp[i+1]);
        }
        ans%=MOD;
        for(int i=0;i<arr.size();i++) s=(s+arr[i])%MOD;
        if(s>0)ans+=s*(k-min(k,2))%MOD;
        return ans%MOD;
    }
};