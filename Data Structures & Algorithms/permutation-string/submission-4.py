class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        window_len = len(s1)

        for char in s1:
            count[char] = 1 + count.get(char, 0)
        
        for i in range(len(s2)):
            count_check = {}
            for j in range(i, i + window_len):
                if j == len(s2):
                    break
                count_check[s2[j]] = 1 + count_check.get(s2[j], 0)
            if count_check == count:
                return True
        
        return False
        
        

        