class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        minHeap, visit = [(0, src, -1)], set()

        for start, end, cost in flights:
            adj[start].append((end, cost))
        
        while minHeap:
            cost, port, steps = heapq.heappop(minHeap)

            if port == dst and steps <= k:
                return cost
            
            for nei, price in adj[port]:
                heapq.heappush(minHeap, (cost + price, nei, steps+1))
        
        return -1
                

