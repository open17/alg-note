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

limits = [1000000,500000,200000,100000,50000,20000]
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
        if not node: return 0
        return node.height
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
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
        elif x>=node.key:
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

avl=AVLTree()

# @fstream
@for_t
def solve():
    opt,x=MII()
    if opt==1:
        avl.insert(x)
    elif opt==2:
        avl.delete(x)
    elif opt==3:
        xx=avl.rank(x)
        s=avl.get_size(avl.root)
        k=avl.kth_largest(s-xx+1)
        if k!=x: xx+=1
        print(xx)
    elif opt==4:
        s=avl.get_size(avl.root)
        # x 
        k=avl.kth_largest(s-x+1)
        print(k)
    elif opt==5:
        r=avl.predecessor(x)
        if not r:
            r=-1000000000
        print(r)
    elif opt==6:
        r=avl.successor(x)
        if r is None:
            r=1000000000
        print(r)

solve()