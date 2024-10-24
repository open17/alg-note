#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    bool isLocal(){
        return true;
    }
    int coinChange(vector<int>& coins, int amount) {
        // https://leetcode.cn/problems/coin-change/description/
        // 最小值
        vector<int> f(amount+1,0x3f3f3f);
        f[0]=0;
        for(auto c:coins){
            for(int i=c;i<=amount;i++){
                f[i]=min(f[i],f[i-c]+1);
            }
        }
        return f[amount]!=0x3f3f3f?f[amount]:-1;
    }
    int change(int amount, vector<int>& coins) {
        // https://leetcode.cn/problems/coin-change-ii/description/
        // 方案数
        vector<int> f(amount+1);
        f[0]=1;
        for(auto c:coins){
            for(int i=c;i<=amount;i++){
                f[i]+=f[i-c];
            }
        }
        return f[amount];
    }
    int numSquares(int n) {
        // https://leetcode.cn/problems/perfect-squares/
        // 最小值
        vector<int> a;
        for(int i=1;i<=sqrt(n);i++){
            a.push_back(i*i);
        }
        vector<int> f(n+1,0x3f3f3f);
        f[0]=0;
        for(auto c:a){
            for(int i=c;i<=n;i++){
                f[i]=min(f[i],f[i-c]+1);
            }
        }
        return f[n]!=0x3f3f3f?f[n]:-1;
    }
    string largestNumber(vector<int>& cost, int target) {
        // https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/
        // 直接维护最大整数的转移会爆int64
        // 当然因为数据不大，你可以使用py或者高精逃课（这也是为什么这题1900）
        // 正解: 我们可以先尝试维护答案的位数
        // 然后再带回去寻找背包的解（DAA课上讲过的01背包求具体解思路差不多）
        vector<int> f(target+1,INT_MIN);
        f[0]=0;
        for(int p=cost.size()-1;p>=0;p--){
            int c=cost[p];
            for(int i=c;i<=target;i++){
                f[i]=max(f[i],f[i-c]+1);
            }
        }
        if(f[target]<=0)return "0";
        string ans="";
        int v=target,p=cost.size()-1;
        while(v>=0&&p>=0){
            int c=cost[p];
            while(v>=c&&f[v]==f[v-c]+1){
                ans+='1'+p;
                v-=c;
            }
            p--;
        }
        return ans;
    }
};