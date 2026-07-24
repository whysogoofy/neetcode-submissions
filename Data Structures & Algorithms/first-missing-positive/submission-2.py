from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Out-of-range elements (<= 0 or > n) are set to n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Use index as hash key by marking nums[abs(val) - 1] as negative
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                idx = val - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
        
        # Step 3: First positive value index + 1 is the missing positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        return n + 1