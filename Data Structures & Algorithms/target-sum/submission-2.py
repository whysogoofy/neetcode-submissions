class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(i, total):
            if i ==len(nums):
                return  total == target

            if (i, total) not in cache:
                cache[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

            return cache[(i, total)]

        return backtrack(0, 0)