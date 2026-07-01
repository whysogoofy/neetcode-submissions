class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        L, R, T, B = 0, len(matrix[0]), 0, len(matrix)
        output = []
        
        while L < R and T < B:
            # 1. Move Right across the top row
            for i in range(L, R):
                output.append(matrix[T][i])
            T += 1
            
            # 2. Move Down the rightmost column
            for i in range(T, B):
                output.append(matrix[i][R-1])
            R -= 1
            
            # --- SAFETY CHECK ---
            # If T and B crossed or L and R crossed, stop immediately
            if not (L < R and T < B):
                break
                
            # 3. Move Left across the bottom row
            for i in range(R-1, L-1, -1):
                output.append(matrix[B-1][i])
            B -= 1
            
            # 4. Move Up the leftmost column
            for i in range(B-1, T-1, -1):
                output.append(matrix[i][L])
            L += 1
        
        return output