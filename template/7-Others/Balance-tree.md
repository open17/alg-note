# 其它平衡树

一些算法竞赛中不太会用到的平衡树/模拟平衡树,同时不保证代码的正确性(主要是感觉AVL可能有点问题?)

## AVL  

```py
"""
AVL 平衡二叉树
通过四种旋转来维护平衡
写起来长了点,理解难度还好
"""
import sys
if "PyPy" in sys.version:
    import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

limits = [20000]
for limit in limits:
    try:
        sys.setrecursionlimit(limit)
        break
    except:
        continue 

class AVLNode:
    __slots__ = ('key', 'left', 'right', 'height')
    def __init__(self, key, left=None, right=None, height=0):
        self.key = key
        self.left = left
        self.right = right
        self.height = height

    def __str__(self):
        return 'AVLNode(%s)' % self.key

    def __repr__(self):
        return 'AVLNode(%s)' % self.key

class AVLTree:
    """
    AVL平衡二叉树实现

    >>> avl = AVLTree()
    >>> avl.insert(5)
    >>> avl.insert(3)
    >>> avl.insert(7)
    >>> avl.insert(2)
    >>> avl.insert(4)
    >>> avl.insert(6)
    >>> avl.insert(8)
    >>> avl.successor(3)
    4
    >>> avl.predecessor(7)
    6
    >>> avl.rank(6)
    5
    >>> avl.kth_largest(2)
    7
    >>> avl.delete(4)
    """
    __slots__ = 'root'
    def __init__(self):
        self.root = None
    def get_height(self, node):
        return -1 if not node else node.height
    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)
    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def left_rotate(self, node):
        """
        左旋: 左右等于左(左子树的右节点=左节点),父子交换
        """
        l=node.left
        node.left=l.right
        l.right=node
        self.update_height(node)
        self.update_height(l)
        return l
    def right_rotate(self, node):
        """
        右旋: 右左等于右(右子树的左节点=右节点),父子交换
        """
        r=node.right
        node.right=r.left
        r.left=node
        self.update_height(node)
        self.update_height(r)
        return r
    
    def rebalance(self, node):

        balance = self.get_balance(node)

        # 左-左情况，进行右旋转
        if balance > 1 and self.get_balance(node.left) >= 0:
            node=self.right_rotate(node)

        # 左-右情况，先进行左旋转，再进行右旋转
        elif balance > 1:
            node.left = self.left_rotate(node.left)
            node=self.right_rotate(node)

        # 右-右情况，进行左旋转
        elif balance < -1 and self.get_balance(node.right) <= 0:
            node=self.left_rotate(node)

        # 右-左情况，先进行右旋转，再进行左旋转
        elif balance < -1:
            node.right = self.right_rotate(node.right)
            node=self.left_rotate(node)

        return node
    
    def _BST_insert(self,node,x):
        if not node:
            return AVLNode(x)
        if x<node.key:
            node.left=self._BST_insert(node.left,x)
        elif x>node.key:
            node.right=self._BST_insert(node.right,x)
        return node

    def _insert(self, node,x):
        node=self._BST_insert(node,x)
        if not node: return None
        self.update_height(node)
        node=self.rebalance(node)
        return node
    
    def insert(self, x):
        self.root=self._insert(self.root,x)
    
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def _BST_delete(self,node,x):
        if not node:
            return node
        if x<node.key:
            node.left=self._BST_delete(node.left,x)
        elif x>node.key:
            node.right=self._BST_delete(node.right,x)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self.find_min(node.right)
                node.key = min_node.key
                node.right = self._BST_delete(node.right, min_node.key)
        return node
    
    def _delete(self, node, key):
        node=self._BST_delete(node,key)
        if not node: return None
        self.update_height(node)
        node = self.rebalance(node)
        return node

    def delete(self,key):
        self.root = self._delete(self.root, key)

    def get_size(self, node):
        if not node:
            return 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)
    
    def get_rank(self, node, x):
        if not node:
            return 0

        if x < node.key:
            return self.get_rank(node.left, x)
        elif x > node.key:
            return 1 + self.get_size(node.left) + self.get_rank(node.right, x)
        else:
            return self.get_size(node.left) + 1

    def rank(self, x):
        return self.get_rank(self.root, x)    
    
    def get_kth_largest(self, node, k):
        if not node:
            return None

        size_right = self.get_size(node.right)
        if k <= size_right:
            return self.get_kth_largest(node.right, k)
        elif k == size_right + 1:
            return node.key
        else:
            return self.get_kth_largest(node.left, k - size_right - 1)

    def kth_largest(self, k):
        return self.get_kth_largest(self.root, k)
    
    def get_predecessor(self, node, x):
        if not node:
            return None

        if x <= node.key:
            return self.get_predecessor(node.left, x)
        else:
            predecessor = self.get_predecessor(node.right, x)
            if predecessor is None:
                return node.key
            else:
                return predecessor

    def predecessor(self, x):
        return self.get_predecessor(self.root, x)
    
    def get_successor(self, node, x):
        if not node:
            return None

        if x >= node.key:
            return self.get_successor(node.right, x)
        else:
            successor = self.get_successor(node.left, x)
            if successor is None:
                return node.key
            else:
                return successor

    def successor(self, x):
        return self.get_successor(self.root, x)
    
    def print_tree(self):
        self.print_inorder(self.root)
        print()

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(node, end=" ")
            self.print_inorder(node.right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```


## 模拟B树

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