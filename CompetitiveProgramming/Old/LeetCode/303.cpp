class NumArray {
public:
    vector<int> v;
    NumArray(vector<int>& nums) : v(1, 0) {
        for(auto i : nums) {
            v.push_back(v.back() + i);
        }
    }
    
    int sumRange(int left, int right) {
        return v[right+1] - v[left];
    }
};
