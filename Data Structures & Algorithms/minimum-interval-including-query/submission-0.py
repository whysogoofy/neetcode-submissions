class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for query in queries:
            last_len = float("inf")
            index = -1
            for i in range(len(intervals)):
                curr_len = intervals[i][1] - intervals[i][0] + 1
                if intervals[i][0] <= query and intervals[i][1] >= query and last_len > curr_len:
                    last_len = curr_len
                    index = i

            output.append(last_len if index != -1 else -1)
        
        return output
                
