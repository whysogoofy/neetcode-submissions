class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        cache = {}
        
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i != len(word1) and j == len(word2):
                return len(word1) - i
            if i == len(word1) and j != len(word2):
                return len(word2) - j
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i+1, j+1)
            else:
                replace = 1 + dfs(i+1, j+1)
                insert = 1 + dfs(i, j+1)
                remove = 1 + dfs(i+1, j)
                cache[(i, j)] = min(replace, insert, remove)
            
            return cache[(i, j)]
        
        return dfs(0, 0)
