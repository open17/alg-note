// 也可以用set优化dp转移,练练字典树就是了
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        /*
        f(i,j)
            if i==0: return check(i,j)
            ans=0
            if check(i,j):
                ans|=f(i-1,i-1)
            if j-i+1<=max_s:
                ans|=f(i-1,j)
            return ans
        f(len(s)-1,len(s)-1)
        */
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
                    f[i][j]=check(i,j);
                    continue;
                }
                f[i][j]=0;
                if(check(i,j)){
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