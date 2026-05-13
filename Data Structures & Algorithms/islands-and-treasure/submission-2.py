class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all gates
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: BFS
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                row, col = r + dr, c + dc

                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 2147483647:
                    grid[row][col] = grid[r][c] + 1
                    q.append((row, col))