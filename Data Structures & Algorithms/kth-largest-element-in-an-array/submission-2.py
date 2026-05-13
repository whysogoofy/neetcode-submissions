class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        out = 0
        counter = k
        while counter != 0:
            out = heapq.heappop_max(nums)
            counter -= 1
        
        return out