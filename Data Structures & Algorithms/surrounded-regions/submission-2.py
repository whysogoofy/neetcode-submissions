class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit, border = set(), set()

        for r in range(ROWS):
            if board[r][0] == "O":
                border.add((r, 0))
            if board[r][COLS-1] == "O":
                border.add((r, COLS-1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                border.add((0, c))
            if board[ROWS-1][c] == "O":
                border.add((ROWS-1, c))

        def dfs(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] == "X" or
                board[r][c] == "#"):
                return
            
            board[r][c] = "#"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r, c in border:
            dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
