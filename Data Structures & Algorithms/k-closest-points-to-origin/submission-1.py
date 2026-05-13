class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hashmap = {}

        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            arr = hashmap.get(dist, [])
            arr.append(point)
            hashmap[dist] = arr
            heapq.heappush(heap, dist)
        
        print(heap)
        print(hashmap)
        
        output = []

        while len(output) < k:
            min_dist = heapq.heappop(heap)
            output.append(hashmap[min_dist].pop())
        
        return output