class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = len(s)

        for i in range(len(s)):
            self.expand(i-1, i+1, s)
            self.expand(i, i+1, s)

        return self.count
    
    def expand(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1