class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        res = nums[0]
        lastmax = 0

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] > lastmax:
                res = n
                lastmax = hashmap[n]

        return res