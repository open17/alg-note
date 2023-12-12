import re
import random
import sys
from math import ceil,floor,fmod,gcd,sqrt,inf
from bisect import bisect_left
from collections import defaultdict,Counter,deque,OrderedDict
from functools import cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy
from typing import *
from string import ascii_lowercase, ascii_uppercase

if "PyPy" in sys.version:
    import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

limits = [100000, 10000, 5000, 2000]
for limit in limits:
    try:
        sys.setrecursionlimit(limit)
        break
    except:
        continue 

def fstream(func):
    def wrapper():
        input_file = open('data.in', 'r')
        sys.stdin = input_file
        output_file = open('data.out', 'w')
        sys.stdout = output_file
        func()
        input_file.close()
        sys.stdin = sys.__stdin__
        output_file.close()
        sys.stdout = sys.__stdout__
    return wrapper

input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()
 
def II():
    return int(input())
 
def MII():
    return map(int, input().split())
 
def LI():
    return list(input().split())
 
def LII():
    return list(map(int, input().split()))

def for_t(func):
    def wrapper():
        T=II()
        for _ in range(T):
            func()
    return wrapper

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


    
operations = []


@for_t
def solve():
    opt, x = map(int, input().split())
    operations.append((opt, x))

@fstream
def main():
    solve()
    for opt, x in operations:
        if opt == 1:
            insert_number(x)
        elif opt == 2:
            delete_number(x)
        elif opt == 3:
            rank = query_rank(x)
            print(rank)
        elif opt == 4:
            number = query_number_by_rank(x)
            print(number)
        elif opt == 5:
            predecessor = find_predecessor(x)
            print(predecessor)
        elif opt == 6:
            successor = find_successor(x)
            print(successor)
    

main()