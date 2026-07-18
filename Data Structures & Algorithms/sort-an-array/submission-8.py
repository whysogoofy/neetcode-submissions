from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(low: int, high: int):
            if low >= high:
                return

            # Partition step (Hoare's scheme)
            # Randomized pivot choice prevents worst-case O(N^2) time on sorted lists
            pivot_idx = random.randint(low, high)
            pivot = nums[pivot_idx]
            
            l, r = low - 1, high + 1
            while True:
                while True:
                    l += 1
                    if nums[l] >= pivot:
                        break
                while True:
                    r -= 1
                    if nums[r] <= pivot:
                        break
                
                if l >= r:
                    break
                
                nums[l], nums[r] = nums[r], nums[l]
            
            # r is the split point; everything <= pivot is left of r, everything >= pivot is right
            quicksort(low, r)
            quicksort(r + 1, high)

        quicksort(0, len(nums) - 1)
        return nums