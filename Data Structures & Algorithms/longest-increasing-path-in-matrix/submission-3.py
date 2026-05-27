class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res, cache = 0, {}

        def dfs(i, j):
            if i < 0 or i == ROWS or j < 0 or j == COLS:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            path_right = dfs(i+1, j) if i+1 < ROWS and matrix[i+1][j] > matrix[i][j] else 0
            path_left = dfs(i-1, j) if i-1 >= 0 and matrix[i-1][j] > matrix[i][j] else 0
            path_top = dfs(i, j+1) if j+1 < COLS and matrix[i][j+1] > matrix[i][j] else 0
            path_down = dfs(i, j-1) if j-1 >= 0 and matrix[i][j-1] > matrix[i][j] else 0

            ret = 1 + max(path_right, path_left, path_top, path_down)
            cache[(i, j)] = ret

            return ret 
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in cache:
                    res = max(dfs(i, j), res)
        
        return res
            
