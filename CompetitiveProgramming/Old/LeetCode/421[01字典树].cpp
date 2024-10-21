template <typename T>
void print(const T &t) { cout << t << endl; }
template <typename T, typename... Args>
void print(const T &t, const Args... args)
{
    cout << t << ' ';
    print(args...);
}
class Solution {
public:
    int nxt[(int)5e6+1][2];
    int cnt=0;
    void insert(int v){
        int cur=0;
        for(int i=30;i>=0;i--){
            int p=(v>>i)&1;
            if(!nxt[cur][p])nxt[cur][p]=++cnt;
            cur=nxt[cur][p];
        }
    }
    int get(int v){
        int cur=0,val=0;
        for(int i=30;i>=0;i--){
            int p=(v>>i)&1;
            if(nxt[cur][p^1]){
                cur=nxt[cur][p^1];
                val+=1<<i;
                continue;
            }
            cur=nxt[cur][p];
        }
        return val;
    }
    int findMaximumXOR(vector<int>& nums) {
        int ans=0;
        for(int i=0;i<nums.size();i++){
            ans=max(ans,get(nums[i]));
            insert(nums[i]);
        }
        return ans;
    }
};