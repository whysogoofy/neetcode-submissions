class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        q = deque([])

        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        
        heap = list(hashmap.values())
        heapq.heapify_max(heap)
        t = 0

        while heap or q:
            # print(t, heap, q)
            if q and q[0][1] < t:
                task_exec = q.popleft()
                heapq.heappush_max(heap, task_exec[0])
            
            max_count = heapq.heappop_max(heap) if heap else 0
            if max_count > 1:
                q.append([max_count - 1, t + n])
            t += 1
        
        return t
