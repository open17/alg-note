class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int,int> dic;
        vector<int> a;
        for(auto i:nums){
            if(dic.count(i))dic[i]++;
            else{
                dic[i]=1;
                a.push_back(i);
            }
        }
        sort(a.begin(),a.end());
        int n=a.size();
        int dp[n+5];
        dp[0]=0;
        dp[1]=0;
        for(int i=2;i<=n+1;i++){
            if(i>2&&a[i-3]==a[i-2]-1)dp[i]=max(dp[i-1],dp[i-2]+a[i-2]*dic[a[i-2]]);
            else dp[i]=dp[i-1]+a[i-2]*dic[a[i-2]];
        }
        return dp[n+1];
    }
};