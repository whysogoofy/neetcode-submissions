class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        
        for num in nums:
            res = min(num, res)
            
        return res