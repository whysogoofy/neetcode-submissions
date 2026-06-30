class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        L, R = 0, n-1
        
        while L < R:
            for i in range(R-L):
                index_i, index_j = n-R-1, L+i
                tmp = matrix[index_i][index_j]
                for _ in range(4):
                    save_tmp = matrix[index_j][n-1-index_i]
                    matrix[index_j][n-1-index_i] = tmp
                    tmp = save_tmp
                    tmp_idx = index_i
                    index_i = index_j
                    index_j = n-1-tmp_idx
            L += 1
            R -= 1
                

                    