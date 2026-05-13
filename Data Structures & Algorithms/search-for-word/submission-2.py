class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Base Case: Found the whole word
            if index == len(word):
                return True
            
            # Boundary and Match checks
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[index]):
                return False

            # 1. MARK VISITED: Save the char and hide it
            temp = board[r][c]
            board[r][c] = "#" 

            # 2. EXPLORE: Try all 4 directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # 3. BACKTRACK: Restore the char for other paths
            board[r][c] = temp
            
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False