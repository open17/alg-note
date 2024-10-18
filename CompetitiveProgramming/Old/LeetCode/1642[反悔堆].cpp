class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int> q;
        int now=INT_MAX;
        int cnt=-1;
        for(auto h:heights){
            if(now<h){
                int d=h-now;
                q.push(d);
                bricks-=d;
                while(bricks<0&&ladders>0){
                    bricks+=q.top();
                    q.pop();
                    ladders--;
                }
                if(bricks<0)break;
            }
            now=h;
            cnt++;
        }
        return cnt;
    }
};