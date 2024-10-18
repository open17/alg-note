class Solution {
public:
    int magicTower(vector<int>& nums) {
        long long s=0,hp=1,cnt=0;
        priority_queue<int> h;
        for(auto i:nums){
            s+=i;
            if(i<0)h.push(-i);
            hp+=i;
            if(hp<=0){
                hp+=h.top();
                h.pop();
                cnt++;
            }
        }
        if(s<0)return -1;
        return cnt;
    }
};