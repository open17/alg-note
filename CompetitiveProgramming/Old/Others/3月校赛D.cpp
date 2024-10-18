#include <bits/stdc++.h>
using namespace std;
const int N=3e5+10;
vector<int> g[N];
int dfs(int root,int fa) {
    int ans=1;
    for (auto son: g[root]) {
        if (son!=fa) {
            ans+=dfs(son,root);
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin>>n;
    for (int i = 1; i < n; i++) {
        int a,b;
        cin>>a>>b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    int s=0;
    int m=-1;
    for (auto son: g[1]) {
        int res=dfs(son,1);
        s+=res;
        m=max(m,res);
    }
    cout<<s-m+1<<endl;
    return 0;
}
