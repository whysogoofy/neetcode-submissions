class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        # print(n, "n")

        for num in nums:
            val = (num - n) if num > n else num
            # print(val)
            # print("actual", num, nums[val-1])
            if nums[val-1] <= n:
                nums[val-1] += n
            else:
                return val