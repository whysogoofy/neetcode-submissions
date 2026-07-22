class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        threshold = len(nums) // 3
        res_set = set()

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] > threshold and n not in res_set:
                res_set.add(n)
        
        return list(res_set)