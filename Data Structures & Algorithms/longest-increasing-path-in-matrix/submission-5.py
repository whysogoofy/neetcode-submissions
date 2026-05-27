class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        cache = [[0] * COLS for _ in range(ROWS)]
        
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            
            max_len = 1
            
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i + di, j + dj

                if 0 <= ni < ROWS and 0 <= nj < COLS and matrix[ni][nj] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(ni, nj))
            
            cache[i][j] = max_len
            return max_len
        
        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))