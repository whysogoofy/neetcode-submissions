class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cache = {}

        def dfs(i):
            if i + nums[i] >= len(nums) - 1:
                return 1
            if not nums[i]:
                return float("inf")
            if i in cache:
                return cache[i]
            
            ret = float("inf")
            # print("u=index", i)
            for j in range(i+1, min(len(nums)-1, nums[i]+i)+1):
                # print("in", ret)
                ret = min(dfs(j)+1, ret)
            #     print("in2", ret)
            # print(i, ret)
            cache[i] = ret
            return ret
        
        return dfs(0)
