class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        while True:
            a = (l + r) // 2
            b = half - a - 2

            ALeft = A[a] if a >= 0 else float("-infinity")
            ARight = A[a+1] if a < (len(A) - 1) else float("infinity")
            BLeft = B[b] if b >=0 else float("-infinity")
            BRight = B[b+1] if b < (len(B) - 1) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                else:
                    return (max(BLeft, ALeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = a - 1
            else:
                l = a + 1
            

            