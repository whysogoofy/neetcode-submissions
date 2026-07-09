class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = 0

        for i in range(len(nums)+1):
            if i < len(nums):
                output ^= nums[i]
            output ^= i

        return output
            