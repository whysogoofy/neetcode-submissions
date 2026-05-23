class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [{} for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for curr_total, count in dp[i].items():
                dp[i+1][curr_total + nums[i]] = dp[i+1].get(curr_total + nums[i], 0) + count
                dp[i+1][curr_total - nums[i]] = dp[i+1].get(curr_total - nums[i], 0) + count
        
        return dp[n].get(target, 0)