# 一些待整理的碎碎念

> 可能该部分大部分内容整理后会移动到注意事项/坑部分  

## c++卡常

- `map<int,stl>`的时候stl要引用,否则常数很大

## c++自定义排序

- 堆的自定义
- sort的自定义

## DP反思

对于这题
> 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
> 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。  


下面的dp伪代码就很不好,我老是喜欢这样直接枚举数据,这样会枚举很多无用的分支,退化到次方级别,而且这样就无法用字典树/字符串哈希优化dp的转移(优化=暴力效果)
```cpp
f(cnt,word_i):
    check=s[cnt-len(word[word_i]),cnt-1]==word[word_i]
    if cnt==len(s): return check
    if !check: return 0
    ans=0
    for j in wordDict:
        ans|=f(cnt+len(j),j)
    return ans
```
应该枚举割点,然后检验一下是否成立,而不是直接枚举数据
