class Solution {
public:
    long long numberOfSubarrays(vector<int>& nums) {
        long long ans = 0;
        stack<int> st;
        unordered_map<int, int> d;
        unordered_map<int, long long> cnt;
        //注意这里0x3f3f3f会被卡掉(不够大)
        nums.push_back(INT_MAX);
        for (int i : nums) {
            while (!st.empty() && st.top() < i) {
                int p = st.top();
                st.pop();
                ans += cnt[p];
                d[p] = 0;
                cnt[p] = 0;
            }
            if (!(!st.empty() && st.top() == i)) {
                st.push(i);
            }
            d[i]++;
            cnt[i] += d[i];
        }
        return ans;
    }
};