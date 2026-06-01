class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = set()

        def dfs(i):
            if i + nums[i] >= len(nums) - 1:
                return True
            if i >= len(nums) or not nums[i] or i in cache:
                return False
            
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True
            
            cache.add(i)
            return False
        
        return dfs(0)