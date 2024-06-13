class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int s=nums[0]+nums[1];
        int cnt=0;
        for(int i=0;i<nums.size();i+=2){
            if(nums[i]+nums[i+1]==s)cnt++;
            else break;
        }   
        return cnt;
    }
};