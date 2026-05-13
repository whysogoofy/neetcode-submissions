class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        print(arr)
        output = 0

        if len(arr) % 2 == 0:
            output = (arr[(len(arr) - 1) // 2] + arr[((len(arr) - 1) // 2) + 1]) / 2
        else:
            output = arr[(len(arr) - 1) // 2]

        return output