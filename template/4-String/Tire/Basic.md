# 基础模板

看到多组字符串前缀匹配,你应该第一时间想到字典树

:::code-group

```cpp
const int N=3e5+5;
int nxt[N][26][2];
int cnt = 0;
string s;
For(i, 0, n)
{   
    cin >> s;
    int cur = 0;
    for (int i = 0; i < s.size(); i++)
    {
        int c = s[i] - 'a';
        if (!nxt[cur][c][0])
        {
            nxt[cur][c][0] = ++cnt;
        }
        nxt[cur][c][1]++;
        cur = nxt[cur][c][0];
    }
}
```

```py
"""
其实用nxt数组模拟即可,python最好不要使用class
这里的板子都是比较早期的代码了
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
```

:::