// auto &q 复用内存(卡常)
// count可能会比find慢?
class NumberContainers {
    map<int,int> a;
    map<int,priority_queue<int, vector<int>>>b; 
public:
    NumberContainers() {

    }
    
    void change(int index, int number) {
        a[index]=number;
        b[number].push(-index);
    }
    
    int find(int number) {
        if(!b.count(number))return -1;
        // 下面会超时
        // priority_queue<int, vector<int>> q =b[number];
        auto &q=b[number];
        while(!q.empty()&&(a[-q.top()]!=number)){
            q.pop();
        }
        return q.empty()?-1:-q.top();
    }
};