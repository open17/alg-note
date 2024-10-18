class Solution {
public:
    int jewelleryValue(vector<vector<int>>& frame) {
        int n=frame.size(),m=frame[0].size();
        int dp[n+1][m+1];
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])+frame[i][j];
            }
        }
        return dp[n][m];
    }
};