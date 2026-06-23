class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])
        res, curr = 0, intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            curr_start, curr_end = curr

            res += 0 if start >= curr_end else 1
            curr = [start, end] if start >= curr_end or end < curr_end else curr

        return res
