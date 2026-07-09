class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0 for _ in range(n+1)]
        offset = 0

        for i in range(1, n+1):
            offset = i if not i & (i - 1) else offset 
            output[i] = 1 + output[i-offset]
        
        return output