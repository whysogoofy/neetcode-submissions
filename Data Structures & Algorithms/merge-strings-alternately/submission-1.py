class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for c1, c2 in zip(word1, word2):
            res.append(c1)
            res.append(c2)
        
        # Append whatever is left over from the longer string
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])
        
        return "".join(res)