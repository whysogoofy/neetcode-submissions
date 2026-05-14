class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            max_len = 1
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + dfs(j))
            
            memo[i] = max_len
            return max_len

        result = 0
        for i in range(len(nums)):
            result = max(result, dfs(i))
            
        return result if nums else 0