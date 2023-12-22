from lib.leetcode import *
class Solution:
    """
    VP250 光速坐牢场
    T1,2直接写,2没推公式凭感觉猜公式还WA了一发
    T3看完5分钟整了个DP,结果T掉了
    T4感觉01Tire,但是开摆了
    因为是VP,感觉没什么动力推代码,所以去看题解了
    """
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        按题目模拟即可
        不想用split所以写的复杂一点
        """
        s=set(brokenLetters)
        text+=' '
        new=1
        cnt=0
        for i in text:
            if i==' ':
                if new:
                    cnt+=1
                new=1
            elif not new:
                continue
            elif i in s:
                new=0
        return cnt
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        没数学推公式,凭感觉凑的公式WA了一发,然后推公式才过的
        以后还是直接推公式吧
        """
        # k x
        # x+K*base>=r
        # k>=(r-x)/base
        # c=k+1
        cnt=0
        for i in range(0,len(rungs)):
            if i==0:
                p=rungs[i]
            else:
                p=rungs[i]-rungs[i-1]
            if dist>=p:
                continue
            cnt+=ceil(p/dist)-1
        return cnt
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        DP+转移优化
        说起来我一直不会算记忆化的复杂度,而且我太依赖记忆化了,这玩意的改进改进
        非记忆化虽然麻烦,但是很方便转移的优化
        当然DP T了后我还在想是不是BFS之类的东西
        """
        @cache
        def f(i,lst_c):
            if i==len(points):
                return 0
            v=0
            for c in range(len(points[0])):
                if i!=0:
                    p=abs(lst_c-c)
                else:
                    p=0
                v=max(v,f(i+1,c)+points[i][c]-p)
            return v
        return f(0,0)
    
            