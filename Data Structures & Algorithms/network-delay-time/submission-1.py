class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i+1: [] for i in range(n)}
        visit, timer = set(), 0
        minHeap = [(0, k)]

        for time in times:
            adj[time[0]].append((time[1], time[2]))
        
        while minHeap:
            t, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            timer = max(t, timer)

            for v, w in adj[node]:
                if v not in visit:
                    heapq.heappush(minHeap, (w + t, v))
        
        for node in adj:
            if node not in visit:
                return -1
        
        return timer
   
                
        

        
        
