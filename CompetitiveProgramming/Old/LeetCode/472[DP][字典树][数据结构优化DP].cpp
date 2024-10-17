class Solution {
    int next[300005][26][2];
    int f[30][30];
    int cnt=0;
    int max_s;
public:
    void insert(string w){
        int cur=0;
        for(int i=0;i<w.size();i++){
            int c=w[i]-'a';
            if(!next[cur][c][0])next[cur][c][0]=++cnt;
            if(i==w.size()-1)next[cur][c][1]=1;
            cur=next[cur][c][0];
        }
    }
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        sort(words.begin(), words.end(), [&](string &a, string &b) {
            return a.size() < b.size();
        });
        vector<string>ans;
        for(auto w:words){
            max_s=max(max_s,(int)w.size());
        }
        for(auto w:words){
            if(cnt>0&&wordBreak(w)){
                ans.push_back(w);
            }
            insert(w);
        }
        return ans;
    }
    bool check(int l,int r,string s){
        int cur=0;
        for(int i=l;i<=r;i++){
            int c=s[i]-'a';
            if(!next[cur][c][0])return false;
            if(i==r&&next[cur][c][1]==1)return true;
            cur=next[cur][c][0];
        }
        return false;
    }
    bool wordBreak(string s) {
        int n=s.size();
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(i==0){
                    f[i][j]=check(i,j,s);
                    continue;
                }
                f[i][j]=0;
                if(check(i,j,s)){
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