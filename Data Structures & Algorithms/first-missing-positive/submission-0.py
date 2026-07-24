class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1

        nums.sort()

        for n in nums:
            if res == n:
                res += 1
        
        return res