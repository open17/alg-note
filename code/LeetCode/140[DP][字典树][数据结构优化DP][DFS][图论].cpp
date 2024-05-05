// 可以减枝优化一下
// 与139一样可以用set优化转移,不过练练字典树就是了
class Solution {
vector<int> g[22];
vector<string> ans;
vector<string> path;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int max_s=0;
        int next[20002][26][2];
        memset(next,0,sizeof(next));
        int cnt=0,cur=0;
        for(auto w:wordDict){
            max_s=max(max_s,(int)w.size());
            cur=0;
            for(int i=0;i<w.size();i++){
                int c=w[i]-'a';
                if(!next[cur][c][0])next[cur][c][0]=++cnt;
                if(i==w.size()-1)next[cur][c][1]=1;
                cur=next[cur][c][0];
            }
        }
        auto check = [&s,&next](int l, int r) -> bool {
            int cur=0;
            for(int i=l;i<=r;i++){
                int c=s[i]-'a';
                if(!next[cur][c][0])return false;
                if(i==r&&next[cur][c][1]==1)return true;
                cur=next[cur][c][0];
            }
            return false;
        };
        int n=s.size();
        int f[n][n];
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(i==0){
                    int c=check(i,j);
                    f[i][j]=c;
                    if(c)g[i].push_back(j);
                    continue;
                }
                f[i][j]=0;
                if(check(i,j)){
                    g[i].push_back(j);
                    f[i][j]|=f[i-1][i-1];
                }
                if(j-i+1<=max_s){
                    f[i][j]|=f[i-1][j];
                }
            }
        }
        dfs(s,0);
        return ans;
    }
    void dfs(string s,int i){
        if(i==s.size()){
            string tmp="";
            for(int j=0;j<path.size();j++){
                tmp+=path[j];
                if(j!=path.size()-1)tmp+=" ";
            }
            ans.push_back(tmp);
            return ;
        }

        for(auto j:g[i]){
            path.push_back(s.substr(i,j+1-i));
            dfs(s,j+1);
            path.pop_back();
        }
    }
};