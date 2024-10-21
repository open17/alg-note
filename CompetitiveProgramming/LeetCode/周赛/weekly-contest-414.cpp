class Solution {
public:
    // https://leetcode.cn/contest/weekly-contest-414/
    string convertDateToBinary(string date) {
        // python写的,这里用灵神的补上吧
        auto bin = [](int x) -> string {
            string s = bitset<32>(x).to_string();
            return s.substr(s.find('1'));
        };
        return bin(stoi(date.substr(0, 4))) + "-" +
               bin(stoi(date.substr(5, 2))) + "-" +
               bin(stoi(date.substr(8, 2)));
    }
    int check(vector<int>& start, int d,int v){
        // 0 2 9 9
        // 0 3 
        long long p=start[0];
        for(int i=1;i<start.size();i++){
            long long px=p+v-start[i];
            if(px>d)return 0;
            p=start[i]+max(px,0LL);
        }
        return 1;
    }
    int maxPossibleScore(vector<int>& start, int d) {
        // 0-2 3-5 6-8
        sort(start.begin(),start.end());
        int n=start.size();
        int r=start[n-1]-start[0]+1+d;
        int l=0;
        while(l<r){
            int mid=l+(r-l)/2;
            if(check(start,d,mid))l=mid+1;
            else r=mid;
        }
        return l-1;
    }
    long long findMaximumScore(vector<int>& nums) {
        int n=nums.size();
        ll ans=0;
        ll res=nums[0],idx=0;
        for(int i=1;i<n;i++){
            if(nums[i]>res||i==n-1){
                ans+=res*(i-idx);
                res=nums[i];
                idx=i;
            }
        }
        return ans;
    }
};