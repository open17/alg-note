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
    print(111,read());
    return 0;
}