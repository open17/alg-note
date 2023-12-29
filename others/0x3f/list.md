# 基础题单
> [本部分源自灵神的仓库](https://github.com/EndlessCheng/codeforces-go/blob/master/copypasta/common.go)


力扣题目分类汇总
https://leetcode.cn/circle/article/04PVPY/
https://leetcode.cn/circle/discuss/vEFf96/

枚举右，维护左
- [1. 两数之和](https://leetcode.cn/problems/two-sum/)
   - https://codeforces.com/problemset/problem/702/B
- [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/)
- [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
- [1512. 好数对的数目](https://leetcode.cn/problems/number-of-good-pairs/) 1161
- [2815. 数组中的最大数对和](https://leetcode.cn/problems/max-pair-sum-in-an-array/) 1295
- [2748. 美丽下标对的数目](https://leetcode.cn/problems/number-of-beautiful-pairs/) 1301
- [2342. 数位和相等数对的最大和](https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) 1309
- [1010. 总持续时间可被 60 整除的歌曲](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/) 1377
- [2874. 有序三元组中的最大值 II](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) 1583
    巧妙安排更新顺序，使得 ans，pre_max 只能使用之前的值，从而符合 i<j<k 的要求
- [454. 四数相加 II](https://leetcode.cn/problems/4sum-ii/)
https://leetcode.com/discuss/interview-question/3685049/25-variations-of-Two-sum-question

哈希表
- [2260. 必须拿起的最小连续卡牌数](https://leetcode.cn/problems/minimum-consecutive-cards-to-pick-up/) 1365
- [982. 按位与为零的三元组](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/) 2085
- [面试题 16.21. 交换和](https://leetcode.cn/problems/sum-swap-lcci/)

前缀和
- [1732. 找到最高海拔](https://leetcode.cn/problems/find-the-highest-altitude/)
- [303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)
- [1310. 子数组异或查询](https://leetcode.cn/problems/xor-queries-of-a-subarray/)
- [2615. 等值距离和](https://leetcode.cn/problems/sum-of-distances/) 1793
- [2602. 使数组元素全部相等的最少操作次数](https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/) 1903

前缀和+哈希表（双变量思想）
- [930. 和相同的二元子数组](https://leetcode.cn/problems/binary-subarrays-with-sum/) 1592  *同 560
- [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
- [1524. 和为奇数的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/) 1611
- [974. 和可被 K 整除的子数组（数目）](https://leetcode.cn/problems/subarray-sums-divisible-by-k/) 1676
   - 变形：乘积可以被 k 整除
   - a[i] = gcd(a[i], k) 之后窗口乘积是 k 的倍数就行，不会乘爆
- [523. 连续的子数组和（长度至少为 2 且可被 K 整除）](https://leetcode.cn/problems/continuous-subarray-sum/)
- [1590.（移除最短子数组）使数组和能被 P 整除](https://leetcode.cn/problems/make-sum-divisible-by-p/) 2039
- [525. 连续数组](https://leetcode.cn/problems/contiguous-array/) *转换
- [1124. 表现良好的最长时间段](https://leetcode.cn/problems/longest-well-performing-interval/) 1908 *转换
- [2488. 统计中位数为 K 的子数组](https://leetcode.cn/problems/count-subarrays-with-median-k/) 1999 *转换
- [2949. 统计美丽子字符串 II](https://leetcode.cn/problems/count-beautiful-substrings-ii/)
- [面试题 17.05. 字母与数字](https://leetcode.cn/problems/find-longest-subarray-lcci/)
- [2489. 固定比率的子字符串数](https://leetcode.cn/problems/number-of-substrings-with-fixed-ratio/)（会员题）
https://atcoder.jp/contests/abc233/tasks/abc233_d

前缀和思想 LC1523 https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/
有点数形结合 https://codeforces.com/problemset/problem/1748/C

前缀和的前缀和（二重前缀和）
LC2281 https://leetcode.cn/problems/sum-of-total-strength-of-wizards/
https://atcoder.jp/contests/abc058/tasks/arc071_b

前缀和+异或
- [1177. 构建回文串检测](https://leetcode.cn/problems/can-make-palindrome-from-substring/)
- [1371. 每个元音包含偶数次的最长子字符串](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/)
- [1542. 找出最长的超赞子字符串](https://leetcode.cn/problems/find-longest-awesome-substring/)
- [1915. 最美子字符串的数目](https://leetcode.cn/problems/number-of-wonderful-substrings/)，[题解](https://leetcode.cn/problems/number-of-wonderful-substrings/solution/qian-zhui-he-chang-jian-ji-qiao-by-endle-t57t/)
https://atcoder.jp/contests/abc295/tasks/abc295_d
模 3 & 字符集大小为 n https://codeforces.com/problemset/problem/1418/G

https://leetcode.cn/problems/find-longest-subarray-lcci/
https://codeforces.com/problemset/problem/1296/C

前后缀分解
- [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)
- [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)（[视频讲解](https://www.bilibili.com/video/BV1Qg411q7ia/?t=3m05s)）
  注：带修改的接雨水 https://codeforces.com/gym/104821/problem/M
  - https://www.zhihu.com/question/627281278/answer/3280684055
- [2906. 构造乘积矩阵](https://leetcode.cn/problems/construct-product-matrix/)
- [2256. 最小平均差](https://leetcode.cn/problems/minimum-average-difference/) 1395
- [2483. 商店的最少代价](https://leetcode.cn/problems/minimum-penalty-for-a-shop/) 1495
- [2909. 元素和最小的山形三元组 II](https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/)
- [2874. 有序三元组中的最大值 II](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) 1583
- [2420. 找到所有好下标](https://leetcode.cn/problems/find-all-good-indices/) 1695
- [2167. 移除所有载有违禁货物车厢所需的最少时间](https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) 2219 *DP
- [2484. 统计回文子序列数目](https://leetcode.cn/problems/count-palindromic-subsequences/) 2223
- [2565. 最少得分子序列](https://leetcode.cn/problems/subsequence-with-the-minimum-score/) 2432
- [2552. 统计上升四元组](https://leetcode.cn/problems/count-increasing-quadruplets/) 2433

#### 定长滑动窗口（右边数字为难度分）
- [1456. 定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) 1263
- [2269. 找到一个数字的 K 美丽值](https://leetcode.cn/problems/find-the-k-beauty-of-a-number/) 1280
- [1984. 学生分数的最小差值](https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) 1306
- [643. 子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)
- [1343. 大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) 1317
- [2090. 半径为 k 的子数组平均值](https://leetcode.cn/problems/k-radius-subarray-averages/) 1358
- [2379. 得到 K 个黑块的最少涂色次数](https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) 1360
- [1052. 爱生气的书店老板](https://leetcode.cn/problems/grumpy-bookstore-owner/) 1418
- [2841. 几乎唯一子数组的最大和](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/) 1546
- [2461. 长度为 K 子数组中的最大和](https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/) 1553
- [1423. 可获得的最大点数](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/) 1574
- [2134. 最少交换次数来组合所有的 1 II](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/) 1748
- [2653. 滑动子数组的美丽值](https://leetcode.cn/problems/sliding-subarray-beauty/) 1786
- [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)
- [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
- [2156. 查找给定哈希值的子串](https://leetcode.cn/problems/find-substring-with-given-hash-value/) 2063
- [346. 数据流中的移动平均值](https://leetcode.cn/problems/moving-average-from-data-stream/)（会员题）
- [1100. 长度为 K 的无重复字符子串](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/)（会员题）
- [1852. 每个子数组的数字种类数](https://leetcode.cn/problems/distinct-numbers-in-each-subarray/)（会员题）
https://codeforces.com/problemset/problem/69/E 1800

#### 不定长滑动窗口（求最长/最大）
- [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
   - 翻转至多一个任意子串后的无重复字符的最长子串 https://codeforces.com/contest/1234/problem/F
- [1493. 删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) 1423
- [904. 水果成篮](https://leetcode.cn/problems/fruit-into-baskets/) 1516
- [1695. 删除子数组的最大得分](https://leetcode.cn/problems/maximum-erasure-value/) 1529
- [2841. 几乎唯一子数组的最大和](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/) 1546
- [2024. 考试的最大困扰度](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) 1643
- [1004. 最大连续1的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/) 1656
- [1438. 绝对差不超过限制的最长连续子数组](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) 1672  *需要 SortedList
- [2401. 最长优雅子数组](https://leetcode.cn/problems/longest-nice-subarray/) 1750  *位运算
- [1658. 将 x 减到 0 的最小操作数](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/) 1817
- [1838. 最高频元素的频数](https://leetcode.cn/problems/frequency-of-the-most-frequent-element/) 1876
- [2831. 找出最长等值子数组](https://leetcode.cn/problems/find-the-longest-equal-subarray/) 1976
- [2106. 摘水果](https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/) 2062
- [1610. 可见点的最大数目](https://leetcode.cn/problems/maximum-number-of-visible-points/) 2147
- [159. 至多包含两个不同字符的最长子串](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/)（会员题）
- [340. 至多包含 K 个不同字符的最长子串](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/)（会员题）
与单调队列结合 https://www.luogu.com.cn/problem/P3594

#### 不定长滑动窗口（求最短/最小）
- [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)
- [1234. 替换子串得到平衡字符串](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/) 1878
- [1574. 删除最短的子数组使剩余数组有序](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) 1932
- [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
- [面试题 17.18. 最短超串](https://leetcode.cn/problems/shortest-supersequence-lcci/)
https://codeforces.com/problemset/problem/701/C

#### 不定长滑动窗口（求子数组个数）
- [2799. 统计完全子数组的数目](https://leetcode.cn/problems/count-complete-subarrays-in-an-array/) 1398
- [713. 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k/)
- [1358. 包含所有三种字符的子字符串数目](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/) 1646
- [2302. 统计得分小于 K 的子数组数目](https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/) 1808
- [2537. 统计好子数组的数目](https://leetcode.cn/problems/count-the-number-of-good-subarrays/) 1892
- [2762. 不间断子数组](https://leetcode.cn/problems/continuous-subarrays/) 1940
- [2743. 计算没有重复字符的子字符串数量](https://leetcode.cn/problems/count-substrings-without-repeating-character/)（会员题）
和至少为 k 的子数组个数 https://atcoder.jp/contests/abc130/tasks/abc130_d
其它题目见【前缀和】

#### 多指针滑动窗口
- [930. 和相同的二元子数组](https://leetcode.cn/problems/binary-subarrays-with-sum/) 1592
- [1248. 统计「优美子数组」](https://leetcode.cn/problems/count-number-of-nice-subarrays/) 1624
- [2563. 统计公平数对的数目](https://leetcode.cn/problems/count-the-number-of-fair-pairs/) 1721
- [1712. 将数组分成三个子数组的方案数](https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/) 2079
- [2444. 统计定界子数组的数目](https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/) 2093
- [992. K 个不同整数的子数组](https://leetcode.cn/problems/subarrays-with-k-different-integers/) 2210

入门题 https://codeforces.com/problemset/problem/602/B
入门题 https://codeforces.com/problemset/problem/279/B
https://atcoder.jp/contests/abc229/tasks/abc229_d
LC424 替换后的最长重复字符 有些特殊的滑窗 https://leetcode.cn/problems/longest-repeating-character-replacement/
LC2271 毯子覆盖的最多白色砖块数 需要多思考一点点 https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/
- https://atcoder.jp/contests/abc098/tasks/arc098_b
较为复杂 https://atcoder.jp/contests/abc294/tasks/abc294_e
      - https://ac.nowcoder.com/acm/contest/62033/D
https://codeforces.com/problemset/problem/1208/B
https://codeforces.com/problemset/problem/1765/D
多指针 https://codeforces.com/problemset/problem/895/B
https://codeforces.com/contest/1833/problem/F
计算有多少子数组，其中有至少 k 个相同的数 https://codeforces.com/problemset/problem/190/D
mex https://atcoder.jp/contests/abc194/tasks/abc194_e
https://codeforces.com/problemset/problem/165/C

双序列双指针
LC88 https://leetcode.cn/problems/merge-sorted-array/
LC360（背向双指针）https://leetcode.cn/problems/sort-transformed-array/
LC986 区间列表的交集 https://leetcode.cn/problems/interval-list-intersections/

相向双指针
LC2824 https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
LC923 https://leetcode.cn/problems/3sum-with-multiplicity/
https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/C

同时用到同向双指针和相向双指针的题
https://atcoder.jp/contests/abc155/tasks/abc155_d
- 相似题目 https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/

a[i] + b[j] = target 的方案数
a[i] + b[j] < target 的方案数    相向双指针 https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
a[i] + b[j] > target 的方案数    同上
a[i] - b[j] = target 的方案数
a[i] - b[j] < target 的方案数    滑窗
a[i] - b[j] > target 的方案数    同上
子数组元素和 = < > target 的方案数：用前缀和，转换成上面 a[i] - b[j] 的形式
子序列元素和 = < > target 的方案数：0-1 背包恰好/至多/至少，见 https://www.bilibili.com/video/BV16Y411v7Y6/ 末尾的总结

## 分组循环

https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/solution/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-zuspx/

**适用场景**：按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。

**核心思想**：

- 外层循环负责遍历组之前的准备工作（记录开始位置），和遍历组之后的统计工作（更新答案最大值）。
- 内层循环负责遍历组，找出这一组最远在哪结束。

这个写法的好处是，各个逻辑块分工明确，也不需要特判最后一组（易错点）。以我的经验，这个写法是所有写法中最不容易出 bug 的，推荐大家记住。

- [1446. 连续字符](https://leetcode.cn/problems/consecutive-characters/)
- [1869. 哪种连续子字符串更长](https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/)
- [1957. 删除字符使字符串变好](https://leetcode.cn/problems/delete-characters-to-make-fancy-string/)
- [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/)
- [2038. 如果相邻两个颜色均相同则删除当前颜色](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [1759. 统计同质子字符串的数目](https://leetcode.cn/problems/count-number-of-homogenous-substrings/)
- [2110. 股票平滑下跌阶段的数目](https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/)
- [1578. 使绳子变成彩色的最短时间](https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/)
- [1839. 所有元音按顺序排布的最长子字符串](https://leetcode.cn/problems/longest-substring-of-all-vowels-in-order/)
- [2760. 最长奇偶子数组](https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/)
- [2765. 最长交替子序列](https://leetcode.cn/problems/longest-alternating-subarray/)
- [795. 区间子数组个数](https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/)
LC1887 https://leetcode.cn/problems/reduction-operations-to-make-the-array-elements-equal/
LC1180（会员）https://leetcode.cn/problems/count-substrings-with-only-one-distinct-letter/
LC2257 https://leetcode.cn/problems/count-unguarded-cells-in-the-grid/
- https://atcoder.jp/contests/abc317/tasks/abc317_e
LC2495（会员）逆向思维 https://leetcode.cn/problems/number-of-subarrays-having-even-product/
https://codeforces.com/problemset/problem/1380/C 1400
https://codeforces.com/problemset/problem/620/C 1500
https://codeforces.com/problemset/problem/525/C 1600
https://codeforces.com/problemset/problem/1748/C 1600

巧妙枚举
LC939 https://leetcode.cn/problems/minimum-area-rectangle/
https://codeforces.com/problemset/problem/1181/C
https://codeforces.com/problemset/problem/1626/D
https://codeforces.com/problemset/problem/846/C

贪心及其证明
- [455. 分发饼干](https://leetcode.cn/problems/assign-cookies/)
- [1029. 两地调度](https://leetcode.cn/problems/two-city-scheduling/) 1348
- [2410. 运动员和训练师的最大匹配数](https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/) 1381
- [881. 救生艇](https://leetcode.cn/problems/boats-to-save-people/) 1530
    - https://codeforces.com/problemset/problem/1690/E
    - https://www.lanqiao.cn/problems/4174/learning/?contest_id=135
    - https://codeforces.com/problemset/problem/1765/D
- [2611. 老鼠和奶酪](https://leetcode.cn/problems/mice-and-cheese/) 1663
- [2931. 购买物品的最大开销](https://leetcode.cn/problems/maximum-spending-after-buying-items/) 1822
- [2952. 需要添加的硬币的最小数量](https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/)
    - LC330 https://leetcode.cn/problems/patching-array/
- [2136. 全部开花的最早一天](https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/) 2033
- todo 复习 [2193. 得到回文串的最少操作次数](https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/) 2091
- [1505. 最多 K 次交换相邻数位后得到的最小整数](https://leetcode.cn/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) 2337
https://codeforces.com/problemset/problem/388/A 1400
https://codeforces.com/problemset/problem/1443/C 1400
https://codeforces.com/problemset/problem/864/D 1500
https://codeforces.com/problemset/problem/1691/C
https://codeforces.com/problemset/problem/1369/C
	提示 1：前 k 大的数一定可以作为最大值。且尽量把大的数放在 w[i] = 1 的组中，这样可以计入答案两次。
	如果某个前 k 大的数 x 没有作为最大值（其中一个组的最大值是不在前 k 大中的 y），那么把 x 和 y 交换，
	如果 x 是某个组的最小值，那么交换后 y 必然也是最小值，此时答案不变。
	如果 x 不是某个组的最小值（这个组的最小值是 z）：
		   如果 y 交换后变成了最小值，那么答案变大了 x-z。
		   如果 y 交换后也不是最小值，那么答案变大了 x-y。
	无论如何，这样交换都不会使答案变小，因此前 k 大的数一定可以作为最大值。
	提示 2：然后来说最小值。a 的最小值必然要分到某个组中，为了「跳过」尽量多的较小的数，优先把 a 中较小的数分到 w 较大的组中。所以 a 从小到大遍历，w 从大到小遍历。
https://codeforces.com/problemset/problem/1479/B1 https://codeforces.com/problemset/problem/1479/B2
    https://www.luogu.com.cn/blog/wsyhb/post-ti-xie-cf1479b1-painting-the-array-i
https://codeforces.com/problemset/problem/1804/D
https://codeforces.com/problemset/problem/442/C
    如果 x>=y<=z，那么删除 y 最优
    结束后剩下一个长为 m 的 /\ 形状的序列，由于无法取到最大值和次大值，那么加上剩下最小的 m-2 个数
https://codeforces.com/problemset/problem/1157/C2
https://www.luogu.com.cn/problem/UVA11384 https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=2379
倒序思维 https://codeforces.com/problemset/problem/1707/A
https://codeforces.com/contest/1873/problem/G
https://atcoder.jp/contests/arc147/tasks/arc147_e 难

中位数贪心（右边数字为难度分） // 注：算长度用左闭右开区间思考，算中间值用闭区间思考
为方便描述，将 $\textit{nums}$ 简记为 $a$。
**定理**：将 $a$ 的所有元素变为 $a$ 的**中位数**是最优的。
**证明**：设 $a$ 的长度为 $n$，设要将所有 $a[i]$ 变为 $x$。假设 $a$ 已经从小到大排序。首先，如果 $x$ 取在区间 $[a[0],a[n-1]]$ 之外，那么 $x$ 向区间方向移动可以使距离和变小；同时，如果 $x$ 取在区间 $[a[0],a[n-1]]$ 之内，无论如何移动 $x$，它到 $a[0]$ 和 $a[n-1]$ 的距离和都是一个定值 $a[n-1]-a[0]$，那么去掉 $a[0]$ 和 $a[n-1]$ 这两个最左最右的数，问题规模缩小。不断缩小问题规模，如果最后剩下 $1$ 个数，那么 $x$ 就取它；如果最后剩下 $2$ 个数，那么 $x$ 取这两个数之间的任意值都可以（包括这两个数）。因此 $x$ 可以取 $a[n/2]$。
题单（右边数字为难度分）
- [462. 最小操作次数使数组元素相等 II](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/)
- [2033. 获取单值网格的最小操作数](https://leetcode.cn/problems/minimum-operations-to-make-a-uni-value-grid/) 1672
- [2448. 使数组相等的最小开销](https://leetcode.cn/problems/minimum-cost-to-make-array-equal/) 2005
- [2607. 使子数组元素和相等](https://leetcode.cn/problems/make-k-subarray-sums-equal/) 2071
- [1703. 得到连续 K 个 1 的最少相邻交换次数](https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) 2467
- [LCP 24. 数字游戏](https://leetcode.cn/problems/5TxKeK/)
https://codeforces.com/problemset/problem/710/B 1400

每次取数组中大于 0 的连续一段同时减 1，求使数组全为 0 的最少操作次数
https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/371326/xing-cheng-mu-biao-shu-zu-de-zi-shu-zu-zui-shao-ze/
https://codeforces.com/problemset/problem/448/C

邻项交换（最小代价排序/字典序最小）
LC1665 https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/
https://codeforces.com/problemset/problem/1638/B 1100
https://codeforces.com/problemset/problem/920/C 1400
https://codeforces.com/problemset/problem/435/B 1400
https://codeforces.com/contest/246/problem/A 900
https://atcoder.jp/contests/arc147/tasks/arc147_b
https://atcoder.jp/contests/abc268/tasks/abc268_f
相邻两数之差的绝对值为 1 https://ac.nowcoder.com/acm/contest/65259/C

非邻项交换（最小代价排序/字典序最小）
LC1202 https://leetcode.cn/problems/smallest-string-with-swaps/
LC2948 https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/
https://codeforces.com/contest/252/problem/B
https://codeforces.com/contest/109/problem/D 2000
shift+reverse https://codeforces.com/contest/1907/problem/F

区间与点的最大匹配/覆盖问题
https://www.luogu.com.cn/problem/P2887
https://codeforces.com/problemset/problem/555/B
https://codeforces.com/problemset/problem/863/E

倒序
LC2718 https://leetcode.cn/problems/sum-of-matrix-after-queries/
- 加强版 https://www.luogu.com.cn/problem/P9715        ?contestId=126251

观察、结论
https://codeforces.com/problemset/problem/1442/A
https://codeforces.com/problemset/problem/558/C
https://codeforces.com/problemset/problem/1610/E
https://codeforces.com/problemset/problem/1811/C
https://codeforces.com/problemset/problem/1822/D
https://codeforces.com/problemset/problem/1608/C 对拍找反例

脑筋急转弯
LC1503 https://leetcode.cn/problems/last-moment-before-all-ants-fall-out-of-a-plank/
LC2731 https://leetcode.cn/problems/movement-of-robots/
LC280 https://leetcode.cn/problems/wiggle-sort/
https://codeforces.com/problemset/problem/1009/B 1400
https://codeforces.com/problemset/problem/1169/B 1500
https://codeforces.com/problemset/problem/1763/C 2000
https://atcoder.jp/contests/abc194/tasks/abc194_e
https://atcoder.jp/contests/abc196/tasks/abc196_e
https://www.luogu.com.cn/problem/UVA10881 https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1822

构造
LC767 https://leetcode.cn/problems/reorganize-string/
LC667 https://leetcode.cn/problems/beautiful-arrangement-ii/
LC2573 https://leetcode.cn/problems/find-the-string-with-lcp/ 2682
https://atcoder.jp/contests/arc145/tasks/arc145_a
https://codeforces.com/contest/803/problem/A 1400
https://codeforces.com/problemset/problem/1809/C 1500
贪心 https://codeforces.com/problemset/problem/118/C
分类讨论 https://codeforces.com/problemset/problem/584/C
分类讨论 https://codeforces.com/problemset/problem/708/B
https://codeforces.com/problemset/problem/1554/D 1800
相邻字母在字母表中不相邻 https://codeforces.com/contest/1156/problem/B
棋盘放最多的马 https://codeforces.com/problemset/problem/142/B
两点间恰好 k 条最短路径 http://codeforces.com/problemset/problem/388/B
https://codeforces.com/problemset/problem/327/D
https://codeforces.com/problemset/problem/515/D
度数均为 k 且至少（恰好）有一条割边 https://codeforces.com/problemset/problem/550/D
最短/最长 LIS https://codeforces.com/problemset/problem/1304/D
https://codeforces.com/problemset/problem/1789/D
交互 二分 https://codeforces.com/problemset/problem/1838/F
todo https://codeforces.com/problemset/problem/1823/D
OR 构造 https://atcoder.jp/contests/agc015/tasks/agc015_d

不好想到的构造
https://codeforces.com/contest/1659/problem/D
https://atcoder.jp/contests/abc178/tasks/abc178_f
https://codeforces.com/problemset/problem/1689/E 脑筋急转弯
https://codeforces.com/problemset/problem/1787/E

不变量（想一想，操作不会改变什么）
https://codeforces.com/contest/1775/problem/E 有点差分的味道，想想前缀和
https://atcoder.jp/contests/arc119/tasks/arc119_c 操作不影响交错和
https://codeforces.com/problemset/problem/1365/F 仍然对称

不变量 2（总和）
把一个环形数组切两刀，分成两段，要求相等，求方案数 => 和为 sum(a)/2 的子数组个数
LC494 https://leetcode.cn/problems/target-sum/

分类讨论（部分题是易错题）
https://codeforces.com/problemset/problem/193/A
https://codeforces.com/problemset/problem/489/C
https://codeforces.com/problemset/problem/1605/C
https://codeforces.com/problemset/problem/382/C
https://codeforces.com/problemset/problem/1051/C
https://codeforces.com/problemset/problem/1095/E
https://codeforces.com/problemset/problem/796/C
https://codeforces.com/problemset/problem/1594/F
https://codeforces.com/problemset/problem/1798/E
https://codeforces.com/problemset/problem/1811/F
https://codeforces.com/problemset/problem/1714/F 锻炼代码实现技巧的好题
https://codeforces.com/problemset/problem/1832/D2
https://codeforces.com/contest/1833/problem/G 样例给的挺良心的
https://codeforces.com/problemset/problem/411/C
https://codeforces.com/contest/1516/problem/C
https://codeforces.com/problemset/problem/1763/C
https://codeforces.com/problemset/problem/960/B
https://codeforces.com/problemset/problem/1799/C
https://codeforces.com/problemset/problem/1009/B 1400 脑筋急转弯
https://codeforces.com/contest/1251/problem/B 1400
https://codeforces.com/problemset/problem/1180/B 1500
https://codeforces.com/problemset/problem/750/C 1600 *也有偏数学的做法
https://codeforces.com/problemset/problem/1861/C 1600 好题！
https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
https://atcoder.jp/contests/abc155/tasks/abc155_d
https://atcoder.jp/contests/abc125/tasks/abc125_d
https://atcoder.jp/contests/arc134/tasks/arc134_d 1998

大量分类讨论
https://codeforces.com/problemset/problem/356/C
https://codeforces.com/problemset/problem/460/D
https://codeforces.com/problemset/problem/796/C
https://codeforces.com/problemset/problem/1374/E2
https://codeforces.com/problemset/problem/1647/D
+构造 https://atcoder.jp/contests/arc153/tasks/arc153_c
https://atcoder.jp/contests/agc015/tasks/agc015_d

贡献法
LC979 https://leetcode.cn/problems/distribute-coins-in-binary-tree/ 1709
LC2477 https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/ 2012
LC891 https://leetcode.cn/problems/sum-of-subsequence-widths/
LC1588 https://leetcode.cn/problems/sum-of-all-odd-length-subarrays/
LC2681 https://leetcode.cn/problems/power-of-heroes/
- https://atcoder.jp/contests/arc116/tasks/arc116_b
LC2763 https://leetcode.cn/problems/sum-of-imbalance-numbers-of-all-subarrays/
更多贡献法题目，见 monotone_stack.go
https://codeforces.com/problemset/problem/1648/A 1400 维度独立
https://codeforces.com/problemset/problem/912/D
https://codeforces.com/problemset/problem/915/F
https://codeforces.com/problemset/problem/1208/E
https://codeforces.com/problemset/problem/1691/C
https://codeforces.com/problemset/problem/1777/D 树
https://codeforces.com/problemset/problem/1788/D 好题！
https://codeforces.com/problemset/problem/1789/C 好题！
https://codeforces.com/problemset/problem/1808/D
https://atcoder.jp/contests/abc290/tasks/abc290_e 好题！
https://atcoder.jp/contests/abc159/tasks/abc159_f 与 0-1 背包结合
^+ https://atcoder.jp/contests/abc201/tasks/abc201_e

《灵茶八题》
完整题目列表 & 题解
https://www.luogu.com.cn/blog/endlesscheng/post-ling-cha-ba-ti-ti-mu-lie-biao
+ 表示元素和
^ 表示异或和
所有子数组的 + 的 +
所有子数组的 ^ 的 ^
所有子数组的 ^ 的 +
所有子数组的 + 的 ^
所有子序列的 + 的 +
所有子序列的 ^ 的 ^
所有子序列的 ^ 的 +
所有子序列的 + 的 ^
所有子数组的 ^2 的 + 的 + https://www.nowcoder.com/feed/main/detail/857f180290cd402ea2461b85e94b3db9
- 这里 ^2 表示任意两个数的异或

小模拟
LC2534 https://leetcode.cn/problems/time-taken-to-cross-the-door/
https://atcoder.jp/contests/abc279/tasks/abc279_f

中模拟
https://atcoder.jp/contests/abc319/tasks/abc319_f

其他
删除一个字符 + 删除最长连续前缀 https://codeforces.com/problemset/problem/1430/D
https://codeforces.com/problemset/problem/521/D

合法括号字符串 Regular Bracket Sequence, RBS
https://codeforces.com/problemset/problem/1821/E
https://codeforces.com/problemset/problem/1830/C

= 变成 <= 或者 >=
求前缀和/后缀和
https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

连续性 + 上下界
https://atcoder.jp/contests/arc137/tasks/arc137_b
https://codeforces.com/contest/1695/problem/C