class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            output.append(self.countPer(i))
        
        return output
    
    def countPer(self, num):
        count = 0

        while num:
            num &= num - 1
            count += 1
        
        return count