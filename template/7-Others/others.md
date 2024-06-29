# 更多

> 待整理

## 防hack哈希表

在codeforces中使用哈希表(unordered_map)有几率会被特别构造的数据hack掉

推荐自定义哈希函数

```cpp
#include<unordered_map>
#include<chrono>

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

unordered_map<int, int, custom_hash> mp;
```

## c++自定义排序

- 堆的自定义
- sort的自定义

## c++ 高精度

## c++ 多参数map



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

## 伪平衡树

```py
"""
B树 利用sqlite3模拟
由于sqlite3底层是B树
B树更适合磁盘中的表现,在内存中操作效率不是很高
给卡常很正常
下面的代码最初蒯自luogu提交
"""
import sqlite3

# 创建或连接到数据库
conn = sqlite3.connect(':memory:')  # 使用内存数据库，也可以使用文件
cursor = conn.cursor()

# 创建表
cursor.execute('CREATE TABLE numbers (value INTEGER)')
cursor.execute('CREATE INDEX idx_value ON numbers(value)')

def insert_number(x):
    cursor.execute('INSERT INTO numbers (value) VALUES (?)', (x,))
    conn.commit()

def delete_number(x):
    cursor.execute('SELECT ROWID FROM numbers WHERE value = ? LIMIT 1', (x,))
    row_id = cursor.fetchone()[0]
    cursor.execute('DELETE FROM numbers WHERE ROWID = ?', (row_id,))
    conn.commit()

def query_rank(x):
    cursor.execute('SELECT COUNT(*) FROM numbers WHERE value < ?', (x,))
    rank = cursor.fetchone()[0] + 1
    return rank

def query_number_by_rank(x):
    cursor.execute('SELECT value FROM numbers ORDER BY value LIMIT 1 OFFSET ?', (x-1,))
    result = cursor.fetchone()
    return result[0] if result else None

def find_predecessor(x):
    cursor.execute('SELECT MAX(value) FROM numbers WHERE value < ?', (x,))
    result = cursor.fetchone()[0]
    return result

def find_successor(x):
    cursor.execute('SELECT MIN(value) FROM numbers WHERE value > ?', (x,))
    result = cursor.fetchone()[0]
    return result
```

## 手写汇编

可能比较幽默

```py
from ctypes import *

def translate_asm(asm_code):
    res = b''
    for line in asm_code.split('\n'):
        if not ':' in line or '>:' in line:
            continue
        line = line[line.find(':')+1:].strip()
        line = line[:line.find('   ')].strip()
        for byte in line.split(' '):
            res += int(byte, 16).to_bytes(1, byteorder='little')
    return res

def compile_asm(asm_code, func_type):
    buf = create_string_buffer(translate_asm(asm_code))
    return CFUNCTYPE(func_type)(cast(buf, POINTER(c_void_p)).contents.value)
```