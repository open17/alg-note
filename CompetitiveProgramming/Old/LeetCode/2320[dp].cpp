class Solution {
public:
    int countHousePlacements(int n) {
        int dp[n+5];
        dp[0]=1;
        dp[1]=2;
        for(int i=2;i<n+2;i++){
            dp[i]=((long long)dp[i-2]+dp[i-1])%((int)1e9+7);
        }
        return ((long long)dp[n]*dp[n])%((int)1e9+7);
    }
};