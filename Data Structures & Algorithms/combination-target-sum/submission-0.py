class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, subsets, set_sum):
            if i == len(nums):
                if set_sum == target:
                    output.append(subsets.copy())
                return
            if set_sum == target:
                output.append(subsets.copy())
                return
            if set_sum > target:
                return

            subsets.append(nums[i])
            set_sum += nums[i]
            dfs(i, subsets, set_sum)

            subsets.pop()
            set_sum -= nums[i]
            dfs(i+1, subsets, set_sum)

        dfs(0, [], 0)

        return output