class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        lens = []
        curr_len = 1
        sorted_arr = sorted(nums)
        curr_num = sorted_arr[0]

        # print(sorted_arr)

        for i in range(1, len(sorted_arr)):
            if curr_num == sorted_arr[i] - 1:
                # print(curr_num, sorted_arr[i])
                curr_len += 1
            elif curr_num == sorted_arr[i]:
                curr_num = sorted_arr[i]
                continue
            else:
                lens.append(curr_len)
                curr_len = 1
            curr_num = sorted_arr[i]
        
        lens.append(curr_len)
        
        return max(lens)

            
                