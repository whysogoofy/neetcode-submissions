class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        prefix, res = 0, 0

        for n in nums:
            prefix += n
            if (prefix - k) in hashmap:
                res += hashmap[prefix-k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        return res
