class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(arr: List[int], n: int, i: int):
            """
            Maintains the max-heap property for a subtree rooted at index i.
            n is the total size of the heap.
            """
            largest = i       # Initialize largest as root
            left = 2 * i + 1   # left child index
            right = 2 * i + 2  # right child index

            # See if left child of root exists and is greater than root
            if left < n and arr[left] > arr[largest]:
                largest = left

            # See if right child of root exists and is greater than the largest so far
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Change root if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap

                # Recursively heapify the affected sub-tree
                heapify(arr, n, largest)

        def heapSort(arr: List[int]):
            n = len(arr)

            # Step 1: Build a max heap.
            # We start from the last non-leaf node (n // 2 - 1) and work up to the root.
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # Step 2: Extract elements from the heap one by one
            for i in range(n - 1, 0, -1):
                # Move current root (the maximum element) to the end of the array
                arr[i], arr[0] = arr[0], arr[i]
                
                # Call max heapify on the reduced heap
                heapify(arr, i, 0)

        # Execute the sort in-place
        heapSort(nums)
        return nums