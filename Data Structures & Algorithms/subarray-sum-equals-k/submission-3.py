class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        prefix = res = 0

        for n in nums:
            prefix += n
            res += counts.get(prefix - k, 0)
            counts[prefix] = counts.get(prefix, 0) + 1

        return res