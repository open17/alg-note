# Codeforces Round 967 (Div. 2)
[![link]( https://img.shields.io/badge/Codeforces-Round_967-03a89e?style=for-the-badge&logo=codeforces&logoColor=fff)](https://codeforces.com/contest/2001)

## 概况

一开始太困了（还不小心错过了开始比赛时间），写的很慢，好还紧急喝了一瓶茶，最后还差点给交互题硬控（没怎么写过想复杂了）

## A. Make All Equal

可以直接看出结论： 无论如何都可以删除数字
（从分类讨论和循环数组出发即可证明）

所以我们统计重复最多的数字即可

## B. Generate Permutation

构造题，答案的构造还是很巧妙的

不过不难打表枚举一下前十个，很容易看出当且仅当n为奇数时有合法构造：

$$1,2,3,...,\lfloor n/2 \rfloor , n,n-1,n-2,...,\lceil n/2 \rceil$$

## C. Guess The Tree

首先这是一颗树

然后对于交互返回的答案x，x让a到x和b到x的差最小，则x必然为a到b的最短路径的中点

并且当x=a的时候a与b之间直接相连（注意x不可能等于b因为会优先返回靠近a的）

总所周知，交互题，一般都是二分（

所以结合上诉多点不难想到从a到b的最短路径的中点开始，每次查询的时候将x换为a，可以一直逼近端点，这样二分的构造直到x等于a，此时找到了b的一个相邻父亲（或者相邻儿子，对于无根树无所谓）

时间复杂度为$O(nlogn)$