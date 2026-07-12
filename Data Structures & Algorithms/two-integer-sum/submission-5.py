class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i, n in enumerate(nums):
            if target - n in hashmap:
                return sorted([i, hashmap[target-n]])
                
            hashmap[n] = i