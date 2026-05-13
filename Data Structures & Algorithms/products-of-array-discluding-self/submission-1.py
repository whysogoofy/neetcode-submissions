class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardArray = [1]
        backwardArray = [1]
        output = []

        for i in range(1, len(nums)):
            forwardArray.append(forwardArray[i - 1] * nums[i - 1])
        
        for i in range(len(nums) - 2, -1, -1):
            backwardArray.append(backwardArray[len(nums) - i - 2] * nums[i + 1])

        for i in range(len(nums)):
            output.append(forwardArray[i] * backwardArray[len(nums) - 1 - i])
        
        return output