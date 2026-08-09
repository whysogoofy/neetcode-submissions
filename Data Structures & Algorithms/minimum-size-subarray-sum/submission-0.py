class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)

        for i in range(0, len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        
        l, r = 0, 0
        res = len(nums)+1

        while r < len(nums):
            curr_sum = prefix[r+1] - prefix[l]
            if curr_sum >= target:
                res = min(res, r-l+1)
                l += 1
            else:
                r += 1
        
        return res if res != len(nums)+1 else 0


