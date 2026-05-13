class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        def bracktracking(r, comb, cols, posD, negD):
            if r == n:
                output.append(["".join(row) for row in comb].copy())
                return
            
            for c in range(n):
                if c in cols or (r-c) in posD or (r+c) in negD:    
                    continue
                cols.add(c)
                posD.add(r-c)
                negD.add(r+c)
                comb[r][c] = 'Q'

                bracktracking(r+1, comb, cols, posD, negD)

                cols.remove(c)
                posD.remove(r-c)
                negD.remove(r+c)
                comb[r][c] = '.'
        
        bracktracking(0, [['.' for _ in range(n)] for _ in range(n)], set(), set(), set())

        return output