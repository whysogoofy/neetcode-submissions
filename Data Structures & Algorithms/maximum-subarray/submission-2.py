class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, res = 0, float("-inf")

        for i in range(len(nums)):
            if prefix >= 0:
                prefix += nums[i]
            else:
                prefix = nums[i] 
            res = max(res, prefix)

        return res