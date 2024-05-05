class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p=[0]
        res={'a','e','i','o','u'}
        def check(s):
            return s[0] in res and s[-1] in res
        for i in words:
            p.append(p[-1]+int(check(i)))
        ans=[]
        for l,r in queries:
            ans.append(p[r+1]-p[l])
        return ans
