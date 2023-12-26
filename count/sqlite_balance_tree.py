"""
B树 利用sqlite3模拟
由于sqlite3底层是B树
B树更适合磁盘中的表现,在内存中操作效率不是很高
给卡常很正常
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