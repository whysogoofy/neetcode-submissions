class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0

        for n in nums:
            if not count:
                count, res = 1, n
            elif n == res:
                count += 1
            else:
                count -= 1
        
        return res