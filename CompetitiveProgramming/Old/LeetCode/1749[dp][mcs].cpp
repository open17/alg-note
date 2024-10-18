class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n=nums.size();
        int f1[n+1],f2[n+1];
        f1[0]=0;
        f2[0]=0;
        int ans=0;
        for(int i=0;i<n;i++){
            f1[i+1]=max(f1[i],0)+nums[i];
            f2[i+1]=min(f2[i],0)+nums[i];
            ans=max(ans,f1[i+1]);
            ans=max(ans,-f2[i+1]);
        }
        return ans;
    }
};