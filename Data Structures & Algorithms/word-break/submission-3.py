class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set()
        
        def dfs(i):
            if i in dp:
                return False
            if i == len(s):
                return True
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        return True

            dp.add(i)
            return False
        
        return dfs(0)
                    
        
