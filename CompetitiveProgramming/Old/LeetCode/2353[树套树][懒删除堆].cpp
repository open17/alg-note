// 提升: 还可以先对string排序然后再离散化一下转为int

class FoodRatings {
    // 烹饪方式对应的食物得分集合, 评分+食物
    map<string,priority_queue<pair<int,string>,vector<pair<int,string>>,greater<>>>a;
    // 食物对应的评分
    unordered_map<string,int> f;
    unordered_map<string,string> b;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n=foods.size();
        for(int i=0;i<n;i++){
            f[foods[i]]=-ratings[i];
            a[cuisines[i]].push({-ratings[i],foods[i]});
            b[foods[i]]=cuisines[i];
        }
    }
    
    void changeRating(string food, int newRating) {
        string cui=b[food];
        a[cui].push({-newRating,food});
        f[food]=-newRating;
    }
    
    string highestRated(string cuisine) {
        auto it=a.find(cuisine);
        auto &q=it->second;
        while(!q.empty()&&f[q.top().second]!=q.top().first)q.pop();
        return q.top().second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */