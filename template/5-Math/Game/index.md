# 博弈论

在算法竞赛中博弈以公平组合问题为主，如没有特殊说明，后文一般指公平组合问题的博弈

## 定义

游戏有两个人参与，二者轮流做出决策，双方均知道游戏的完整信息；

任意一个游戏者在某一确定状态可以作出的决策集合只与当前的状态有关，而与游戏者无关；

游戏中的同一个状态不可能多次抵达，游戏以玩家无法行动为结束，且游戏一定会在有限步后以非平局结束。


## 性质

一般非打表的话我们会从这些性质入手开始分析博弈的思路

- 没有后继状态的状态是必败状态。
- 一个状态是必胜状态当且仅当存在至少一个必败状态为它的后继状态
- 一个状态是必败状态当且仅当它的所有后继状态均为必胜状态
