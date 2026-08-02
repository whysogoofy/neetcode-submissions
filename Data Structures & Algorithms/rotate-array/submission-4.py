class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
            
        def reverse(l, r):
            for i in range(l, (l+r+1)//2):
                nums[i], nums[l+r-i] = nums[l+r-i], nums[i]
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

