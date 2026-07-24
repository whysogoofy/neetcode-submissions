class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_val = len(nums)
        
        # taking out negative numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # buidling the hashset
        for n in nums:
            if not n or abs(n) > max_val:
                continue
            
            index = abs(n) - 1
            
            if not nums[index]:
                nums[index] = -1
            elif nums[index] > 0:
                nums[index] *= -1
        
        # check for possible solution in range (1, len(nums) + 1)
        for i in range(0, len(nums)):
            if nums[i] >= 0:
                return i+1
        
        return len(nums) + 1