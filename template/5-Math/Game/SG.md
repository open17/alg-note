# SG函数

对于绝大部分公平组合问题都可以转换为有向图游戏

SG函数可以定义为:

$SG(x)=mex(SG(y)|x\rightarrow y)$

若 $SG(x)=0$ 先手必败，反之必胜

这样我们可以较为暴力的构建一个博弈图

但是你可能会有疑问，现在除了细化了具体的每个状态的值，复杂度可能还要比正常直接推转移要高？（毕竟相对01多了更多的细化博弈状态）

SG函数方便的地方在于它对于组合型博弈（可以拆分为子游戏的）存在以下定理：

$$SG(x)=Xor(SG(y)|x\rightarrow y)$$

我们可以把SG(x)视为Nim博弈的堆来推导出这个结论（棋子往SG值大的方向移动时等价于放回，也不影响决策）

## 例题

[P10501](https://www.luogu.com.cn/problem/P10501)


:::details 代码
```cpp
int mex(auto S) 
{
    for (int i = 0;; ++i)
        if (S.find(i) == S.end())
            return i;
}

void solve()
{
    /*
        要注意当sg的w或者h为1的时候不适用SG定理
        因为一个为1的所有都是成功态，子节点也不是失败态，不符合公平组合的定义
        所以规定从2开始计算
    */
    int h,w;
    while(cin>>w>>h){
        vector<vector<int>> sg(w+1,vector<int>(h+1));
        rep(i,2,w+1)
            rep(j,2,h+1){
                unordered_set<int> s;
                if(i<=3&&j<=3)continue;
                rep(p,2,i-1)s.insert(sg[p][j]^sg[i-p][j]);
                rep(p,2,j-1)s.insert(sg[i][p]^sg[i][j-p]);
                sg[i][j]=mex(s);
            }
        print(sg[w][h]?"WIN":"LOSE");
    }
}
```
:::