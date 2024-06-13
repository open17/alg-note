class Solution {
public:
    int addRungs(vector<int>& rungs, int dist) {
        int cnt=0;
        int s=0;
        for(int i=0;i<rungs.size();i++){
            int d=rungs[i]-s;
            s=rungs[i];
            cnt+=max((d-1)/dist,0);
        }
        return cnt;
    }
};