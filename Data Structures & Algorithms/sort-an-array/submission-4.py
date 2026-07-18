class Solution:
    # bubble sort
    def sortArray(self, nums: List[int]) -> List[int]:
        swapped = False
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums)-1-i):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        
        return nums