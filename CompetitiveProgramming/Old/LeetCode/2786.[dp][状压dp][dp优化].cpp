class Solution {
public:
    long long maxScore(vector<int>& nums, int x) {
        long long f[2];
        f[(nums[0]&1)^1]=-0x3f3f3f;
        f[nums[0]&1]=nums[0];
        for(int i=1;i<nums.size();i++){
            int p=nums[i]&1;
            f[p]=max(f[p],f[p^1]-x)+nums[i];
        }
        return max(f[0],f[1]);
    }
};