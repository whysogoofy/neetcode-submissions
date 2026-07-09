class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to restrict numbers to 32 bits
        mask = 0xFFFFFFFF
        
        while b & mask:  # Use 'b' as the carry
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # If 'a' is a negative number in 32-bit two's complement form, 
        # we need to convert it back to a Python negative integer.
        # 0x7FFFFFFF is the maximum positive value for a 32-bit signed int.
        return (a & mask) if (a & mask) <= 0x7FFFFFFF else ~((a & mask) ^ mask)
        