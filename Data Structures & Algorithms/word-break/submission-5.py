class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dp.get(i+len(word), False):
                        dp[i] = True
                        break
            
            if i not in dp:
                dp[i] = False
        
        return dp[0]
        
