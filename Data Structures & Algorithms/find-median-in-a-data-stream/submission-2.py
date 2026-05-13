class MedianFinder:

    def __init__(self):
        self.heap_left = []
        self.heap_right = []
        
    def addNum(self, num: int) -> None:
        left_max = self.heap_left[0] if self.heap_left else float("infinity")
        right_min = self.heap_right[0] if self.heap_right else float("-infinity")
        if left_max >= num:     heapq.heappush_max(self.heap_left, num)
        else:                   heapq.heappush(self.heap_right, num)

        while len(self.heap_left) - len(self.heap_right) > 1:
            tmp = heapq.heappop_max(self.heap_left)
            heapq.heappush(self.heap_right, tmp)
        
        while len(self.heap_right) > len(self.heap_left):
            tmp = heapq.heappop(self.heap_right)
            heapq.heappush_max(self.heap_left, tmp)

    def findMedian(self) -> float:
        if len(self.heap_left) == len(self.heap_right):
            med = (self.heap_left[0] + self.heap_right[0]) / 2
            return med
        else:
            return self.heap_left[0]
        
        