class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = float("-inf")

        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                output = max(output, product)
        
        return output
