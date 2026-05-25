class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False

        # 1D DP array representing rows of s1
        dp = [False] * (len1 + 1)
        dp[len1] = True # Base case

        # Initialize the last row (matching only s1 characters against s3)
        for j in range(len1 - 1, -1, -1):
            dp[j] = dp[j + 1] and s1[j] == s3[len2 + j]

        # Process remaining rows from bottom to top
        for i in range(len2 - 1, -1, -1):
            # Update the last element of the row (matching only s2)
            dp[len1] = dp[len1] and s2[i] == s3[i + len1]
            
            # Update columns from right to left
            for j in range(len1 - 1, -1, -1):
                ans = False
                if s1[j] == s3[i + j] and dp[j + 1]:
                    ans = True
                if s2[i] == s3[i + j] and dp[j]:
                    ans = True
                dp[j] = ans

        return dp[0]