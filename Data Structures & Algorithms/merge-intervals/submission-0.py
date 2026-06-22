class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        res, curr = [], intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            curr_start, curr_end = curr
            if curr_end < start:
                res.append(curr)
                curr = [start, end]
            else:
                curr = [min(start, curr_start), max(end, curr_end)]
        
        res.append(curr)

        return res

            