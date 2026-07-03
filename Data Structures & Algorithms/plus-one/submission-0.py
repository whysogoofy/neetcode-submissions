class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                if carry:
                    digits[i] += 1
                    carry = 0
                break
            else:
                if carry:
                    digits[i] = 0
                else:
                    break
        
        return digits if not carry else [1] + digits