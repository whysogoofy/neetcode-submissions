class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r, c):
            visit.add((r, c))
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                next_dirts = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for rd, cd in next_dirts:
                    new_r, new_c = row + rd, col + cd

                    if (new_r in range(ROWS) and new_c in range(COLS) and
                    ((new_r, new_c) not in visit) and grid[new_r][new_c] == '1'):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        
        ROWS, COLS = len(grid), len(grid[0])
        islands, visit = 0, set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and ((r, c) not in visit):
                    dfs(r, c)
                    islands += 1
        
        return islands