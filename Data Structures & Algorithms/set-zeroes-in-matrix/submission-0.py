class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        z_rows, z_cols = set(), set()

        for i in range(ROWS):
            for j in range(COLS):
                if not matrix[i][j]:
                    z_rows.add(i)
                    z_cols.add(j)
        
        for i in z_rows:
            for j in range(COLS):
                matrix[i][j] = 0
        
        for j in z_cols:
            for i in range(ROWS):
                matrix[i][j] = 0
            


        