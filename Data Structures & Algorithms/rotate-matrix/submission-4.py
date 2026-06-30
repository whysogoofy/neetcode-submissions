class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Loop through layers from outside in
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                # Simultaneous 4-way swap
                (
                    matrix[i][j],
                    matrix[j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[n - 1 - j][i]
                ) = (
                    matrix[n - 1 - j][i],       # Bottom-left to Top-left
                    matrix[i][j],               # Top-left to Top-right
                    matrix[j][n - 1 - i],       # Top-right to Bottom-right
                    matrix[n - 1 - i][n - 1 - j] # Bottom-right to Bottom-left
                )