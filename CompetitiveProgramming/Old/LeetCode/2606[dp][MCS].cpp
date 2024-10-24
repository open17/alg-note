class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        int v[26];
        for(int i=0;i<26;i++)v[i]=i+1;
        for(int i=0;i<chars.size();i++)v[chars[i]-'a']=vals[i];
        int n=s.size(),ans=0;
        int dp[n+1];
        dp[0]=0;
        for(int i=0;i<n;i++){
            dp[i+1]=max(dp[i],0)+v[s[i]-'a'];
            ans=max(ans,dp[i+1]);
        }
        return ans;
    }
};