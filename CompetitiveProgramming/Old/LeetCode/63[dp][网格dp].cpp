class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n=obstacleGrid.size(),m=obstacleGrid[0].size();
        int dp[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(obstacleGrid[i][j]){
                    dp[i][j]=0;
                    continue;
                }
                if(i==0&&j==0){
                    dp[i][j]=1;
                    continue;
                }
                if(i==0){
                    dp[i][j]=dp[i][j-1];
                    continue;
                }
                if(j==0){
                    dp[i][j]=dp[i-1][j];
                    continue;
                }
                dp[i][j]=dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[n-1][m-1];
    }
};