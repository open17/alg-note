// (标签这么说显得很高级就是了
// 其实还是很基础的一道题(分数才1500,不过个人觉得lazy删除堆的写法更好写一点)
// python的话如果这么写就比较麻烦了(不用sorted库就要手搞平衡树了)
// 因为强制在线还要多开一个map(数据范围很大),请分清每个map对应的下标
// 哈希表套平衡树也行,都可以做


class NumberContainers {
map<int,int> a;
map<int,set<int>>b;
public:
    NumberContainers() {
    }
    
    void change(int index, int number) {
        auto idx=a.find(index);
        if(idx!=a.end()){
            b[idx->second].erase(index);
            idx->second=number;
        }
        else a[index]=number;
        b[number].insert(index);
    }
    
    int find(int number) {
        auto idx=b.find(number);
        if(idx==b.end()||idx->second.empty())return -1;
        return *(idx->second.begin());

    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */