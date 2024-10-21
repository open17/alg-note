#include "bits/stdc++.h"
using namespace std;

// 板子开始

template <typename T>
struct Fenwick {
    int n;
    std::vector<T> a;
    
    Fenwick(int n_ = 0) {
        init(n_);
    }
    
    void init(int n_) {
        n = n_;
        a.assign(n, T{});
    }
    
    void add(int i, const T &v) {
        while(i<n) {
            a[i]+=v;
            i+=i&-i;
        }
    }
    
    T get(int i) {
        T ans{};
        while(i>0){
            ans+=a[i];
            i-=i&-i;
        }
        return ans;
    }
    
    T range(int l, int r) {
        return get(r)-get(l-1);
    }
    
    int selectKth(const T &k) {
        int x = 0;
        T cur{};
        for (int i = 1 << std::__lg(n); i; i /= 2) {
            if (x + i <= n && cur + a[x + i - 1] <= k) {
                x += i;
                cur = cur + a[x - 1];
            }
        }
        return x;
    }
};


template <typename T>
struct Discrete{
    vector<T> arr;
    Discrete(){}
    Discrete(vector<T> &arr){
        this->arr=arr;
        clear();
    }
    void add(T val){
        arr.push_back(val);
    }
    void clear(){
        sort(arr.begin(),arr.end());
        arr.erase(unique(arr.begin(),arr.end()),arr.end());
    }
    T get(T v){
        return lower_bound(arr.begin(),arr.end(),v)-arr.begin();
    }
};

// 板子结束

class Solution {
public:
    vector<int> resultArray(vector<int> &nums) {
        // https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/description/
        auto sorted = nums;
        Discrete<int> d=Discrete(sorted);
        int m = d.arr.size();
        vector<int> a{nums[0]}, b{nums[1]};
        Fenwick<int> t1(m + 1), t2(m + 1);
        t1.add(d.get(nums[0]) + 1,1);
        t2.add(d.get(nums[1]) + 1,1);
        for (int i = 2; i < nums.size(); i++) {
            int x = nums[i];
            int v = d.get(x)+1;
            int gc1 = a.size() - t1.range(1,v);
            int gc2 = b.size() - t2.range(1,v);
            if (gc1 > gc2 || gc1 == gc2 && a.size() <= b.size()) {
                a.push_back(x);
                t1.add(v,1);
            } else {
                b.push_back(x);
                t2.add(v,1);
            }
        }
        a.insert(a.end(), b.begin(), b.end());
        return a;
    }
    int createSortedArray(vector<int>& instructions) {
        // https://leetcode.cn/problems/create-sorted-array-through-instructions/
        int ans=0;
        int mod=1e9+7;
        int n=1e5+5;
        Fenwick<long long> fw(n);
        for(auto p:instructions){
            p++;
            int a=fw.range(1,p-1);
            int b=fw.range(p+1,n-1);
            ans+=min(a,b)%mod;
            ans%=mod;
            fw.add(p,1);
        }
        return ans;
    }
}