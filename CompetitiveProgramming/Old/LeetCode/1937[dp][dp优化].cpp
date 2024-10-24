class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        // dp[i][j]=max(dp[i][j],dp[i-1][j+d]-abs(d))
        int n=points.size();
        int m=points[0].size();
        long long dp[n][m];
        memset(dp,0,sizeof(dp));
        long long ans=-1;
        for(int i=0;i<n;i++){
            long long lm=0,rm=0;
            for(int j=0;j<m;j++){
                if(i==0)break;
                lm=max(dp[i-1][j],lm-1);
                dp[i][j]=max(dp[i][j],lm);
            }
            for(int j=m-1;j>=0;j--){
                if(i==0)break;
                rm=max(dp[i-1][j],rm-1);
                dp[i][j]=max(dp[i][j],rm);
            }
            for(int j=0;j<m;j++){
                dp[i][j]+=points[i][j];
                if(i==n-1){ans=max(ans,dp[i][j]);}
            }
        }
        return ans;
    }
};