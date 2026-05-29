class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        dp = {}

        def dfs(L, R):
            if (L, R) in dp:
                return dp[(L, R)]
            if L > R:
                return 0
            if L == R:
                return nums[L-1]*nums[L]*nums[L+1]
            
            ret = 0
            for i in range(L, R+1):
                ret = max(ret, dfs(L, i-1) + nums[L-1]*nums[i]*nums[R+1] + dfs(i+1, R))

            dp[(L, R)] = ret
            return ret
    
        return dfs(1, len(nums)-2)
        
       
            



            