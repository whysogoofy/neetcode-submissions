from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Find up to two potential candidates
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                # Decrement both when a third distinct element is found
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates with actual counts
        result = []
        threshold = len(nums) // 3

        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)

        return result