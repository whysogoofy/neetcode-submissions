class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = {0: 0, 1: 0, 2: 0}
        i = 0

        for n in nums:
            bucket[n] += 1
        
        for key in bucket:
            for _ in range(bucket[key]):
                nums[i] = key
                i += 1