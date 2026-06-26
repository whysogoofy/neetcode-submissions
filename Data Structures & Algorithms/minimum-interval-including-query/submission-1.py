class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda item: item[0])
        qs = sorted(queries)
        index, hashmap, minHeap = 0, {}, []

        for query in qs:
            while index < len(intervals):
                start, end = intervals[index]
                if start <= query and query <= end:
                    heapq.heappush(minHeap, (end - start + 1, end))
                if intervals[index][0] > query:
                    break    
                index += 1
            
            while minHeap:
                if minHeap[0][1] >= query:
                    hashmap[query] = minHeap[0][0]
                    break
                else:
                    heapq.heappop(minHeap)
                
            if not minHeap:
                hashmap[query] = -1

        output = []

        for q in queries:
            output.append(hashmap[q])

        return output
