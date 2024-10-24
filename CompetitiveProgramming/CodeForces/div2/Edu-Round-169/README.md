# Educational Codeforces Round 169 (Rated for Div. 2)
[![link]( https://img.shields.io/badge/Codeforces-Round_169-blue?style=for-the-badge&logo=codeforces&logoColor=fff)](https://codeforces.com/contest/2004)

## 概况

打的小唐

## A. Closest Point

反正数据范围挺小的，暴力枚举点即可

## B. Game with Doors

画画图，显然相交的地方加上门然后端点处理一下

一开始以为a,b,c,d一定有序，没处理WA了

## C. Splitting Items

显然A必然取最大，B取次大，以此往复

所以可以得到贪心决策：

狠狠的贪心尽量让次大和最大一样大

## D. Colored Portals

手玩可以得到结论：

4种门，每个点两种门，如果两个点之间可达，必然只至多只通过一个中转门

然后预处理一下每个点的16种点的左边的位置和右边的位置

如果两个点可以直接到达就输出

否则寻找中转门，按照预处理的位置找最小即可

还有一个小性质就是16种点只有一种和当前点不可达，所以枚举点的时候只用判断中转点不等于目标点即可