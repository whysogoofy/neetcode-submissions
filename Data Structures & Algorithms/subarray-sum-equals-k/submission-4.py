from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = res = 0

        for n in nums:
            prefix += n
            res += counts[prefix - k]  # Defaults to 0 if key doesn't exist
            counts[prefix] += 1

        return res