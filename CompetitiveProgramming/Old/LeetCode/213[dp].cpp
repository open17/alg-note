class Solution {
public:
    int dp(vector<int>& nums,int epx,int n){
        if(n<=0)return 0;
        int f[n+2];
        f[0]=0;
        f[1]=0;
        for(int i=0;i<n;i++){
            f[i+2]=max(f[i+1],f[i]+nums[i+epx]);
        }
        return f[n+1];
    }
    int rob(vector<int>& nums) {
        int n=nums.size();
        return max(dp(nums,1,n-1),dp(nums,2,n-3)+nums[0]);
    }
};