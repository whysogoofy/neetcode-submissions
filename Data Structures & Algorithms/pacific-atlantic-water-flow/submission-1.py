class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pcfc, atlnt, visit = set(), set(), set()

        for r in range(ROWS):
            pcfc.add((r, 0))
            atlnt.add((r, COLS-1))
        
        for c in range(COLS):
            pcfc.add((0, c))
            atlnt.add((ROWS-1, c))

        def dfs(r, c, ocean, prev):
            if (r < 0 or r == ROWS or c < 0 
                or c == COLS or prev > heights[r][c]
                or (r, c) in visit):
                return
            
            visit.add((r, c))
            if ocean:
                pcfc.add((r, c))
            else:
                atlnt.add((r, c))
            
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])
        
        for r, c in list(pcfc):
            dfs(r, c, 1, heights[r][c])
            visist = set()
        
        for r, c in list(atlnt):
            dfs(r, c, 0, heights[r][c])
            visit = set()
        
        return list(pcfc & atlnt)