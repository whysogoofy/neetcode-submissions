class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i, j = 1, 1
        last = nums[0]

        while j < len(nums):
            if last != nums[j]:
                last = nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
        return i