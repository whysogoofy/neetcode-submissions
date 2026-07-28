class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2 = 0, 0
        output = ""

        while i1 < len(word1) and i2 < len(word2):
            output += word1[i1]
            output += word2[i2]
            i1 += 1
            i2 += 1
        
        while i1 < len(word1):
            output += word1[i1]
            i1 += 1

        while i2 < len(word2):
            output += word2[i2]
            i2 += 1
        
        return output
