class Solution:
    def checksum(self, x: int, y: int, target: int) -> bool:
        if(x + y == target):
            return True
        else:
            return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) == 2):
            if(self.checksum(nums[0], nums[1], target)):
                return [0, 1]
            
        # mid = len(nums) // 2

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if(self.checksum(nums[i], nums[j], target)):
                    return [i, j]