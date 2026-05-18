class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for j in range(m-1, -1, -1):
            for i in range(n-1, -1, -1):
                if text2[j] == text1[i]:
                    dp[j][i] = dp[j+1][i+1] + 1
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i+1])
        
        return dp[0][0]