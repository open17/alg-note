class Solution {
public:
    int nxt[(int)3e5+10][2][2];
    int cnt=0,root=-1;
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        int n=parents.size();
        vector<int> g[n+1];
        vector<pair<int,int>> s[n+1];
        vector<int> ans(queries.size());
        memset(nxt,0,sizeof(nxt));
        int idx=0;
        for(auto p:queries){
            // move 1
            s[p[0]+1].push_back({p[1],idx++});
        }
        // move 1
        for(int i=0;i<n;i++){
            if(parents[i]+1==0)root=i+1;
            g[parents[i]+1].push_back(i+1);
        }
        dfs(root,g,s,ans);
        return ans;
    }
    void insert(int v){
        int cur=0;
        for(int i=30;i>=0;i--){
            int p=(v>>i)&1;
            if(!nxt[cur][p][0])nxt[cur][p][0]=++cnt;
            nxt[cur][p][1]++;
            cur=nxt[cur][p][0];
        }
    }
    void del(int v){
        int cur=0;
        for(int i=30;i>=0;i--){
            int p=(v>>i)&1;
            nxt[cur][p][1]--;
            cur=nxt[cur][p][0];
        }
    }
    int get(int v){
        int cur=0,val=0;
        for(int i=30;i>=0;i--){
            int p=(v>>i)&1;
            if(nxt[cur][p^1][1]>0){
                cur=nxt[cur][p^1][0];
                val+=1<<i;
                continue;
            }
            cur=nxt[cur][p][0];
        }
        return val;
    }
    void dfs(int node,vector<int> g[],vector<pair<int,int>> s[],vector<int> &ans){
        insert(node-1);
        for(auto p:s[node]){
            ans[p.second]=get(p.first);
        }
        for(auto child:g[node]){
            // print("parent",node-1,"child",child-1);
            dfs(child,g,s,ans);
        }
        del(node-1);
    }
};