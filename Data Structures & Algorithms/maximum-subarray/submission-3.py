class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, res = 0, float("-inf")

        for i in range(len(nums)):
            prefix += nums[i] if prefix >= 0 else nums[i] - prefix
            res = max(res, prefix)

        return res