# Codeforces Round 966 (Div. 3)
[![link]( https://img.shields.io/badge/Codeforces-Round_966-8A2BE2?style=for-the-badge&logo=codeforces&logoColor=fff)](https://codeforces.com/contest/2000)

## 概况

很久没打比赛了，VP的状态很差，经常被很简单的小问题卡一下

## A. Primary Task

模拟

## B. Seating in a Bus

模拟

维护区间左右端点即可，写的时候没细想直接用set维护座位也行

## C. Numeric String Template

从左到右只用维护上一个是否相同即可

VP的时候没想好，想直接处理所有相同的字符的下标出来然后两面查，WA了好多发

另外怕哈希被hack，就贴了个离散化

## D. Right Left Wrong

双指针维护找LR即可

## E. Photoshoot for Gorillas

推一下每个格子的贡献，然后按照贡献大小贪心的填高度

贡献有个公式写错了推了半天，其实都是左端点以为是右端点XD