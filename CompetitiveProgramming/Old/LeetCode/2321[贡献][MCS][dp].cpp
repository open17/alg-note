class Solution {
public:
    int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(),s1=0,s2=0;
        int dp[n+1][2],res=0,res2=0;
        dp[0][0]=0;
        dp[0][1]=0;
        for(int i=0;i<n;i++){
            s1+=nums1[i];
            s2+=nums2[i];
            int tmp=nums1[i]-nums2[i];
            dp[i+1][0]=max(dp[i][0],0)+tmp;
            dp[i+1][1]=min(dp[i][1],0)+tmp;
            res=max(res,dp[i+1][0]);
            res2=min(res2,dp[i+1][1]);
        }
        return max(s1-res2,s2+res);
    }
};