class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minHeap, visit = [(grid[0][0], (0, 0))], set({})

        while minHeap:
            t, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            if node == (ROWS-1, COLS-1):
                return max(t, grid[node[0]][node[1]])
            visit.add(node)

            dirts = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for rd, cd in dirts:
                row, col = node[0] + rd, node[1] + cd
                if row >= 0 and row < ROWS and col >= 0 and col < COLS:
                    heapq.heappush(minHeap, (max(t, grid[row][col]), (row, col)))


            
