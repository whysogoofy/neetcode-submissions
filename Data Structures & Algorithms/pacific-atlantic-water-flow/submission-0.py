class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visit, res = set(), set()

        def dfs(r, c, prev):
            if r < 0 or c < 0:
                return (1, 0)
            elif r == ROWS or c == COLS:
                return (0, 1)
            if (r, c) in visit or prev < heights[r][c]:
                return (0, 0)
            
            visit.add((r, c))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            bool_out = [0, 0]

            for rd, cd in dirs:
                row, col = r + rd, c + cd
                ret = dfs(row, col, heights[r][c])
                bool_out[0] = ret[0] or bool_out[0]
                bool_out[1] = ret[1] or bool_out[1]
            
            # print("dfs_res", r,c ,prev, heights[r][c], bool_out)
            if bool_out[0] and bool_out[1]:
                res.add((r, c))
            
            return tuple(bool_out)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in res:
                    # print("call_dfs", r, c)
                    dfs(r, c, heights[r][c])
                    visit = set()
        # dfs(0, 0, heights[0][0])
        
        return list(res)