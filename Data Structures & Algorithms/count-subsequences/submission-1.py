class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]

        for i in range(len(s)+1):
            dp[-1][i] = 1
        
        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                dp[i][j] = dp[i][j+1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        print(dp)
        return dp[0][0]