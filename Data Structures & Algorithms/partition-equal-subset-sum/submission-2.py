class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, dp = sum(nums), set([0])
        half = total//2

        if total % 2:
            return False

        for i in range(len(nums)-1, -1, -1):
            copy = dp.copy()
            for val in copy:
                tol = val + nums[i]
                if tol == half:
                    return True
                dp.add(tol)
        
        return False

            