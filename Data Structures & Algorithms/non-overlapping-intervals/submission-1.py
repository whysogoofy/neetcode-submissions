class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])
        res, curr = 0, intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            curr_start, curr_end = curr
            
            if start >= curr_end:
                curr = [start, end]
            else:
                res += 1
                if end < curr_end:
                    curr = [start, end]

        return res
