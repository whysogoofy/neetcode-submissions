class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Serves as both our write-pointer and our count

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k