class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        l, i, r = 0, 0, len(nums)-1

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                if l == i:
                    i += 1
                    continue
                l += 1
            if nums[i] == 2:
                swap(i, r)
                r -= 1
            if nums[i] == 1:
                i += 1