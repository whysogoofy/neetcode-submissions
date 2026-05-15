class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, dp = sum(nums), set()
        half = total//2

        if total % 2:
            return False

        def dfs(i, curr_sum, subset):
            # print(i, curr_sum, subset)
            if curr_sum == half and i != len(nums) - 1 and len(subset) != len(nums):  
                return True
            if curr_sum in dp:
                return False
            
            for j in range(len(nums)):
                if j != i and j not in subset:
                    subset.add(j)
                    if dfs(j, curr_sum + nums[j], subset):
                        return True
                    subset.remove(j)
            
            dp.add(curr_sum)
            return False

        for i in range(len(nums)):
            # print(dp)
            if dfs(i, nums[i], set([i])):
                return True
        
        return False