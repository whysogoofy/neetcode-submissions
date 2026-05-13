class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def rename():
            for r, c in visit:
                board[r][c] = "X"

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return False
            if board[r][c] == "X" or (r, c) in visit:
                return True
            
            visit.add((r, c))

            return (dfs(r+1, c) and
                    dfs(r-1, c) and
                    dfs(r, c+1) and 
                    dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if dfs(r, c):
                        rename()
                    visit = set()