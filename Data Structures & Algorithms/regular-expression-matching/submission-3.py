class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                elif match:
                    dp[i][j] = dp[i+1][j+1]
        
        return dp[0][0]