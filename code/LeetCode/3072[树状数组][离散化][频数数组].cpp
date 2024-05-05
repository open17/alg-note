class Solution {
    vector<int> tree;
public:
    int lowbit(int x){return x&(-x);}
    void add(int i,int v,int n){
        while(i<n){
            tree[i]+=v;
            i+=lowbit(i);
        }
    }
    int query(int i){
        int ans=0;
        while(i>0){
            ans+=tree[i];
            i-=lowbit(i);
        }
        return ans;
    }
    vector<int> resultArray(vector<int>& nums) {
        auto s=nums;
        ranges::sort(s);
        s.erase(unique(s.begin(),s.end()),s.end());
        int n=s.size();
        tree.resize(n+5);
        auto get=[&s](int v) -> int {
            return s.end()-ranges::lower_bound(s,v);
        };
        vector<int> a{nums[0]}, b{nums[1]};
        add(get(nums[0]),1,n);
        add(get(nums[1]),-1,n);
        for(int i=2;i<nums.size();i++){
            int idx=get(nums[i]);
            int ans=query(idx-1);
            if(ans>0||ans==0&&a.size()<=b.size()){
                a.push_back(nums[i]);
                add(idx,1,n);
            }
            else{
                b.push_back(nums[i]);
                add(idx,-1,n);
            }
        }
        a.insert(a.end(),b.begin(),b.end());
        return a;
    }
};