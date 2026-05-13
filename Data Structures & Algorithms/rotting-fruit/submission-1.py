class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        self.total_fresh, time = 0, -1

        def addOrange(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS
                or grid[r][c] != 1):
                return
            # print("inside")
            q.append((r, c))
            grid[r][c] = 2
            # print(self.total_fresh)
            self.total_fresh -= 1
            # print(self.total_fresh)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    self.total_fresh += 1
        
        if not self.total_fresh:
            return 0
        
        # print(q)
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addOrange(r+1, c)
                addOrange(r-1, c)
                addOrange(r, c+1)
                addOrange(r, c-1)
            time += 1
        
        # print(self.total_fresh, grid)
        return time if not self.total_fresh else -1
        