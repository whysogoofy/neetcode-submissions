class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        def sum_sq(num):
            total = 0
            for char in str(num):
                integer = int(char)
                total += integer * integer
            return total
        
        res = sum_sq(n)
        
        while not (res == 1 or res in hashset):
            hashset.add(res)
            res = sum_sq(res)
        
        return res == 1
        