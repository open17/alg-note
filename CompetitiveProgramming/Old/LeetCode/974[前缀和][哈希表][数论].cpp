class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int>a(1,0);
        // 小心负数取模问题
        for(auto i:nums)a.push_back((a.back()+(i%k+k)%k)%k);
        map<int,int>m;
        int ans=0;
        for(auto v:a){
            cout<<v<<endl;
            if(m.count(v))ans+=m[v];
            else{
                m[v]=0;
            }
            m[v]++;
        }
        return ans;
    }
};