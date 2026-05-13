class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        minHeap = [(0, 0)] 
        total_cost = 0

        while len(visit) < n:
            dist, i = heapq.heappop(minHeap)

            if i in visit:
                continue
            
            visit.add(i)
            total_cost += dist
            
            curr_x, curr_y = points[i]

            for j in range(n):
                if j not in visit:
                    d = abs(curr_x - points[j][0]) + abs(curr_y - points[j][1])
                    heapq.heappush(minHeap, (d, j))
            
        return total_cost