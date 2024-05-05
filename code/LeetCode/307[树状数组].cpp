class NumArray {
private:
    vector<int> nums;
    vector<int> tree;
    int lowbit(int i){
        return i&(-i);
    }
    int prefixSum(int i) {
        int s=0;
        while(i>0){
            s+=tree[i];
            i-=lowbit(i);
        }
        return s;
    }

public:
    NumArray(vector<int> &nums) : nums(nums.size()), tree(nums.size() + 1) {
        for (int i=0;i<nums.size();i++) {
            update(i,nums[i]);
        }
    }

    void update(int index, int val) {
        int delta=val-nums[index];
        nums[index]=val;
        for (int i=index+1; i<tree.size(); i+=lowbit(i)) {
            tree[i]+=delta;
        }
    }

    int sumRange(int left, int right) {
        return prefixSum(right+1)-prefixSum(left);
    }
};