class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        // dp为平方级
        sort(courses.begin(), courses.end(), [](vector<int> a, vector<int> b) {return a[1] < b[1];});
        priority_queue<int> q;
        int now=0;
        int cnt=0;
        for(auto c:courses){
            int d=c[0],lst=c[1];
            if(now+d>lst){
                // 思考为什么不是now+d-q.top()<=lst?
                if(!q.empty() && d<q.top()){
                    now-=q.top();
                    q.pop();
                    cnt--;
                }
                else{
                    continue;
                }
            }
            now+=d;
            q.push(d);
            cnt++;
        }
        return cnt;
    }
};