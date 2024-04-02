"""
字典树(前缀树) 常用于字符串匹配
当然特殊的子类01tire常用于解决XOR最大问题和平衡树模拟
同时后缀树也是一种特殊的前缀树
"""

class Tire_Node:
    __slot__=['child','end']
    def __init__(self,end=False):
        self.child={}
        self.end=end

class Trie:
    __slot__=['root']
    
    def __init__(self):
        self.root=Tire_Node()

    def insert(self, word: str) -> None:
        node=self.root
        for i in word:
            if i not in node.child.keys():
                node.child[i]=Tire_Node()
            node=node.child[i]
        node.end=True
        
    def search(self, word: str) -> bool:
        node=self.root
        for i in word:
            if i not in node.child.keys():
                return False
            node=node.child[i]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for i in prefix:
            if i not in node.child.keys():
                return False
            node=node.child[i]
        return True