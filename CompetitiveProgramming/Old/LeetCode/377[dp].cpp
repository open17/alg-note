class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // f[i]=sum(f[i-nums[k]])
        sort(nums.begin(),nums.end());
        long MOD=1;
        MOD<<=32;
        int n=target;
        int f[n+1];
        memset(f,0,sizeof(f));
        f[0]=1;
        for(int i=1;i<=n;i++){
            for(int k=0;k<nums.size();k++){
                if(i-nums[k]<0)break;
                f[i]+=f[i-nums[k]]%MOD;
                f[i]%=MOD;
            }
        }
        return f[n];
    }
};