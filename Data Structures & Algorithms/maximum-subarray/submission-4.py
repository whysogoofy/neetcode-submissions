class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            
            current_sum += num
            if current_sum > res:
                res = current_sum

        return res