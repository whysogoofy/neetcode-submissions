import random

class Solution:
    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            rand_idx = random.randint(low, high)
            swap(arr, rand_idx, high)
            pivot = arr[high]
            i = low - 1
            
            # traverse arr[low..high] and move all smaller
            # elements to the left side. Elements from low to 
            # i are smaller after every iteration
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    swap(arr, i, j)
            
            # move pivot after smaller elements and
            # return its position
            swap(arr, i + 1, high)
            return i + 1

        # swap function
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        # the QuickSort function implementation
        def quickSort(arr, low, high):
            if low < high:
                
                # pi is the partition return index of pivot
                pi = partition(arr, low, high)
                
                # recursion calls for smaller elements
                # and greater or equals elements
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)
        
        quickSort(nums, 0, len(nums)-1)

        return nums