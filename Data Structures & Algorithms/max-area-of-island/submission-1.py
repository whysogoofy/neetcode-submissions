class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea, visit = 0, set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) 
                or (r, c) in visit or not grid[r][c]):
                return 0

            visit.add((r, c))
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea