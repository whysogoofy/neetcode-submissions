class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        self.maxArea, visit = 0, set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            visit.add((r, c))
            q = deque([(r, c)])
            area = 1

            while q:
                row, col = q.popleft()
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for rd, cd in dirs:
                    r_new, c_new = row + rd, col + cd

                    if (r_new in range(ROWS) and c_new in range(COLS)
                        and (r_new, c_new) not in visit and grid[r_new][c_new] == 1):
                        q.append((r_new, c_new))
                        visit.add((r_new, c_new))
                        area += 1
            self.maxArea = max(self.maxArea, area)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r, c)
        
        return self.maxArea