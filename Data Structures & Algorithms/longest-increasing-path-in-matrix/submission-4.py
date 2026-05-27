class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [[1] * COLS for _ in range(ROWS)]

        cells = []
        for r in range(ROWS):
            for c in range(COLS):
                cells.append((matrix[r][c], r, c))
                
        cells.sort(key=lambda x: x[0])
        
        max_path = 1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for val, r, c in cells:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > val:
                    dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)
                    max_path = max(max_path, dp[nr][nc])
                    
        return max_path