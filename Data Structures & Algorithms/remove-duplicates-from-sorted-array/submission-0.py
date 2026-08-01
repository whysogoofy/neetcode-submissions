class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        i = 1
        k = len(nums)
        
        while True:
            if i == len(nums):
                break
            if nums[i] == nums[i-1]:
                nums.pop(i)
                k -= 1
                continue
            i += 1
        
        return k
