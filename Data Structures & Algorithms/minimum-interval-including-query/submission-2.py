class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda item: item[0])
        
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        minHeap = []
        index = 0
        n = len(intervals)
        
        for query, original_idx in sorted_queries:
            while index < n and intervals[index][0] <= query:
                start, end = intervals[index]
                heapq.heappush(minHeap, (end - start + 1, end))
                index += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
                
            if minHeap:
                res[original_idx] = minHeap[0][0]
                
        return res