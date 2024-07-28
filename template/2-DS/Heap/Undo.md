# 反悔堆

## 什么是


用堆实现的反悔贪心,主要是利用堆来反悔一些直接的贪心决策


## 举个例子

要最小化决策数量,一种决策代价低但是效果差(1-10效果,同种之间值不定),一种决策代价高但是效果好(100-200效果),我们先贪心的选代价低的决策,然后当不行的时候反悔最小的效果的决策并改为高代价的决策

## 例题

[题目](https://leetcode.cn/problems/minimum-number-of-refueling-stops/description/)

```cpp
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
```