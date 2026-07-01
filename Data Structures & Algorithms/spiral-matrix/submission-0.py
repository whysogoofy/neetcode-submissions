class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        L, R, T, B = 0, len(matrix[0]), 0, len(matrix)
        output = []
        
        while L < R and T < B:
            for i in range(L, R):
                output.append(matrix[T][i])
            T += 1
            for i in range(T, B):
                output.append(matrix[i][R-1])
            R -= 1
            
            if not (L < R and T < B):
                break

            for i in range(R-1, L-1, -1):
                output.append(matrix[B-1][i])
            B -= 1
            for i in range(B-1, T-1, -1):
                output.append(matrix[i][L])
            L += 1
        
        return output