class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            res = self.expand(s, i, i, res)

            res = self.expand(s, i, i + 1, res)
            
        return res

    def expand(self, s: str, l: int, r: int, current_res: str) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(current_res):
                current_res = s[l : r + 1]
            l -= 1
            r += 1
        return current_res