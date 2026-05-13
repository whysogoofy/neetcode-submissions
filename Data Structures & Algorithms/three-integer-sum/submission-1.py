class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        comb_map = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        key = tuple(sorted([nums[i], nums[j], nums[k]]))
                        comb_map[key] = comb_map.get(key, [nums[i], nums[j], nums[k]])
        
        return list(comb_map.values())
        