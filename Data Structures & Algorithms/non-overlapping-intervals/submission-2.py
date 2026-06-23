from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        # Greedy Choice: Sort by end times
        intervals.sort(key=lambda item: item[1])
        
        res = 0
        curr_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # If the current interval starts BEFORE the last one ends, it's an overlap!
            if start < curr_end:
                res += 1  # We must erase this interval
            else:
                # No overlap, update our end tracker to the current interval's end
                curr_end = end
                
        return res