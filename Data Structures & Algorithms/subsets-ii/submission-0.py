class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        def dfs(i, subset):
            if i == len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            tmp = nums[i]
            while i < len(nums) and tmp == nums[i]:
                i += 1
            dfs(i, subset)

        dfs(0, [])

        return output