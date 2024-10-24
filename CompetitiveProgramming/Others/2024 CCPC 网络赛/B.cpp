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
    int n = read();
    unordered_map<int, int> m;
    int mm=0;
    // int a[n+5];
    vector<int> a;
    for(int i = 0; i < n; i++) {
        int tmp= read();
        if(!m.count(tmp))a.push_back(tmp);
        m[tmp]++;
        mm=max(mm,m[tmp]);
    }
    sort(a.begin(),a.end());
    int len=a.size();
    long long ans = 0;
    for(int i = 0; i < len; i++) {
        for(int j = i + 1; j < len; j++) {
            // print(a[j] - a[i],i,j,m[a[i]],m[a[j]]);
            ans += (a[j] - a[i])*m[a[i]]*m[a[j]];
        }
    }
    cout << ans << " ";
    int MOD=998244353;
    int res=1;
    if(ans!=0)res++;
    vector<int> A(mm+1);
    A[1]=1;
    for(int i=2;i<=mm;i++){
        A[i]=(A[i-1]*(i%MOD))%MOD;
    }
    for(auto p:a){
        res=(res*A[m[p]])%MOD;
    }
    print(res);
    return 0;
}