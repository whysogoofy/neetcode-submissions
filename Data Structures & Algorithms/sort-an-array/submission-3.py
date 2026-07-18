class Solution:
    # merge sort
    def merge(self, left, right):
        l, r = 0, 0
        arr = []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])
                r += 1
        
        while l < len(left):
            arr.append(left[l])
            l += 1
        
        while r < len(right):
            arr.append(right[r])
            r += 1

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums)//2
        
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])

        return self.merge(left, right)
        
