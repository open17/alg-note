class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int,int> mp;
        vector<long long> a;
        for(auto p:power){
            mp[p]++;
            if(mp[p]==1){
                a.push_back(p);
            }
        }
        sort(a.begin(),a.end());
        int n=a.size();
        long long f[n+3];
        memset(f,0,sizeof(f));
        for(int i=0;i<n;i++){
            f[i+3]=f[i]+a[i]*mp[a[i]];
            if(i>=1&&a[i]-a[i-1]<=2)f[i+3]=max(f[i+3],f[i+2]);
            else f[i+3]=max(f[i+3],f[i+2]+a[i]*mp[a[i]]);
            if(i>=2&&a[i]-a[i-2]<=2)f[i+3]=max(f[i+3],f[i+1]);
            else f[i+3]=max(f[i+3],f[i+1]+a[i]*mp[a[i]]);
        }
        return f[n+2];
    }
};