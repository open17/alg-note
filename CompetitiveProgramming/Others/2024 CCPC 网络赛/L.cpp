#include <bits/stdc++.h>
#define int long long
#define ll long long
#define endl '\n'
#define pii pair<int,int>
using namespace std;

template <typename T> void print(const T &t){
    cout<<t<<endl;
}

template<typename T,typename ...Args> void print(const T &t,const Args... args){
    cout<<t<<" ";
    print(args...);
}

ll qpow(ll a,ll n,ll mod ){
    ll ans=1;
    a%=mod;
    while(n){
        if(n&1)ans=(ans*a)%mod;
        a=(a*a)%mod;
        n>>=1;
    }
    return ans;
}

ll inv(ll a,ll mod){
    return qpow(a,mod-2,mod);
}



int read(){
    int x=0,f=1;
    char c=getchar();
    while(c<'0'||c>'9'){
        if(c=='-')f=-1;
        c=getchar();
    }
    while(c<='9'&&c>='0'){
        x=x*10+(c-'0');
        c=getchar();
    }
    return x*f;
}

signed main(){
    int n=read(),m=read();
    vector<vector<char>> s(n,vector<char>(m));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            s[i][j]=getchar();
        }
        getchar();
    }
    int ans=0;
    for(int i=1;i<n;i++){
        for(int j=0;j<m-1;j++){
            if(s[i][j]=='p'&&s[i-1][j]=='c'&&s[i-1][j+1]=='c'&&s[i][j+1]=='c'){
                ans++;
            }
        }
        getchar();
    }
    print(ans);
    return 0;
}