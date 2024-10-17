class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int next[4005][26][2];
        memset(next,0,sizeof(next));
        int cnt=0;
        int n=strs.size();
        string ans="";
        for(auto s:strs){
            int cur=0;
            for(int i=0;i<s.size();i++){
                int c=s[i]-'a';
                if(!next[cur][c][0]){
                    next[cur][c][0]=++cnt;
                }
                next[cur][c][1]++;
                if(next[cur][c][1]==n)ans+=s[i];
                cur=next[cur][c][0];
            }
        }
        return ans;
    }
};