class Solution {
public:
    int lengthOfLongestSubsequence(vector<int>& nums, int target) {
        // f(i)=f(i-nums[j])+1
        int f[target+1];
        memset(f,-0x3f,sizeof(f));
        f[0]=0;
        for(int j=0;j<nums.size();j++){
            for(int i=target;i>=nums[j];i--){
                f[i]=max(f[i],f[i-nums[j]]+1);
            }
        }
        return f[target]>0?f[target]:-1;
    }
};