class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a=text.split()
        s=set()
        for i in brokenLetters:
            s.add(i)
        cnt=0
        for i in a:
            for j in i:
                if j in s:
                    break
            else:
                cnt+=1
        return cnt