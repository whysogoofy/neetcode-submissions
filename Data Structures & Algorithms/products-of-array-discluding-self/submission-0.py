class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        isZero = 0
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                isZero += 1
        
        output = []

        for num in nums:
            if num != 0:
                if isZero > 0:
                    output.append(0)
                else:
                    output.append(prod//num)
            else:
                if isZero == 1:
                    output.append(prod)
                else:
                    output.append(0)
        
        return output