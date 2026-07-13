class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                # Instead of swapping, just copy the element from the right
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        
        # 'l' naturally ends up equal to the number of valid elements
        return l