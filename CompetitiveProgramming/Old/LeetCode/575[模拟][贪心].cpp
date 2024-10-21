class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> s;
        for(auto candy:candyType){
            s.insert(candy);
        }
        return min(candyType.size()/2,s.size());
    }
};