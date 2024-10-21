class Solution {
    int f[30][30];
    int max_s;
    unordered_set<string> st;
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        sort(words.begin(), words.end(), [&](string &a, string &b) {
            return a.size() < b.size();
        });
        vector<string>ans;
        for(auto w:words){
            max_s=max(max_s,(int)w.size());
        }
        for(auto w:words){
            if(!st.empty()&&wordBreak(w)){
                ans.push_back(w);
            }
            st.insert(w);
        }
        return ans;
    }
    bool wordBreak(string s) {
        int n=s.size();
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(i==0){
                    f[i][j]=st.count(s.substr(i,j-i+1));
                    continue;
                }
                f[i][j]=0;
                if(st.count(s.substr(i,j-i+1))){
                    f[i][j]|=f[i-1][i-1];
                }
                if(j-i+1<=max_s){
                    f[i][j]|=f[i-1][j];
                }
            }
        }
        return f[n-1][n-1];
    }
};