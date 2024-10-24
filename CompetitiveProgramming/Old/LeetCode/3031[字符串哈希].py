class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        思维转换
        """
        # 最坏情况
        
        s=word
        # 哈希板子
        n=len(s)
        ans=ceil(n/k)

        random.seed()
        MOD1 = 998244353 + random.randint(0, 10007)
        MOD2 = int(1e9+7) + random.randint(0, 233)
        BASE1 = 33 + random.randint(0, 233)
        BASE2 = 133 + random.randint(0, 53)

        b1 = [1]
        b2 = [1]
        h1 = [0]
        h2 = [0]

        for i in range(n):
            b1.append(b1[i] * BASE1 % MOD1)
            b2.append(b2[i] * BASE2 % MOD2)
            h1.append((h1[i] * BASE1 % MOD1 + ord(s[i]) - ord('a')) % MOD1)
            h2.append((h2[i] * BASE2 % MOD2 + ord(s[i]) - ord('a')) % MOD2)  

        # 从0开始,左闭右闭
        def query(l, r):
            hash1 = (h1[r + 1] - h1[l] * b1[r - l + 1] % MOD1 + MOD1) % MOD1
            hash2 = (h2[r + 1] - h2[l] * b2[r - l + 1] % MOD2 + MOD2) % MOD2
            return hash1, hash2


        def check(a,b):
            return query(0,a)==query(b,n-1)

        for t in range(1,ans):
            if check(n-t*k-1,t*k):
                return t
        return ans
            


