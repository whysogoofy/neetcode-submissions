class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_prod, max_prod = 1, 1

        for num in nums:
            if not num:
                max_prod, min_prod = 1, 1
                continue

            prod1, prod2 = min_prod*num, max_prod*num
            
            max_prod, min_prod = max(prod1, prod2, num), min(prod1, prod2, num)
            res = max(max_prod, res)
        
        return res