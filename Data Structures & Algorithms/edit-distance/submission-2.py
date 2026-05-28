class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        cache = [[float("inf")] * len(word2) for _ in range(len(word1))]
        
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i != len(word1) and j == len(word2):
                return len(word1) - i
            if i == len(word1) and j != len(word2):
                return len(word2) - j
            if cache[i][j] != float("inf"):
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dfs(i+1, j+1)
            else:
                dirs = [(1, 1), (0, 1), (1, 0)]

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    cache[i][j] = min(1 + dfs(ni, nj), cache[i][j])
            
            return cache[i][j]
        
        return dfs(0, 0)
