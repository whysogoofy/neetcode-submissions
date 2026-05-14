class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = { (len(nums)-1): [1, nums[-1]] }

        for i in range(len(nums)-2, -1, -1):
            length = 1
            for j in range(i+1, len(nums)):
                if nums[i] < dp[j][1]:
                    length = max(length, 1 + dp[j][0])
            res = max(res, length)
            dp[i] = [length, nums[i]]
        
        return res if nums else 0