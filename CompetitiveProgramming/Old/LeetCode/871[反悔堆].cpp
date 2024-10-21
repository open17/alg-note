class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        vector<int> end(2);
        end[0]=target;
        end[1]=0;
        stations.push_back(end);
        sort(stations.begin(),stations.end());
        priority_queue<int> q;
        int cnt=0;
        int now=0;
        for(auto s:stations){
            int pos=s[0],fuel=s[1];
            if(pos>target)break;
            int d=pos-now;
            while(!q.empty()&&startFuel<d){
                startFuel+=q.top();
                q.pop();
                cnt++;
            }
            if(startFuel<d)return -1;
            startFuel-=d;
            now=pos;
            q.push(fuel);
        }
        return cnt;
    }
};