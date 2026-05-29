class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        dp = [[-1] * len(nums) for _ in range(len(nums))]

        def dfs(L, R):
            if dp[L-1][R-1] >= 0:
                return dp[L-1][R-1]
            if L > R:
                return 0
            if L == R:
                return nums[L-1]*nums[L]*nums[L+1]
            
            ret = 0
            for i in range(L, R+1):
                ret = max(ret, dfs(L, i-1) + nums[L-1]*nums[i]*nums[R+1] + dfs(i+1, R))

            dp[L-1][R-1] = ret
            return ret
    
        return dfs(1, len(nums)-2)
        
       
            



            