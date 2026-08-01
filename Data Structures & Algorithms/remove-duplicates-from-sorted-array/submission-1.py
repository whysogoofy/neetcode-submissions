class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        l, r = 1, len(nums) - 1
        k = len(nums)

        while l <= r:
            if nums[l-1] == nums[l]:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                k -= 1

                i = l
                while i < r and nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i += 1
            else:
                l += 1
        # print(nums, len(nums) - 1 - r)
        return k