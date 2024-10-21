class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        vector<int>px;
        for(auto p:points){
            px.push_back(p[0]);
        }
        sort(px.begin(),px.end());
        int base=px[0];
        int ans=1;
        for(auto p:px){
            if (w+base<p){
                ans+=1;
                base=p;
            }
        }
        return ans;
    }
};