class Solution:
    def countSubstrings(self, s: str) -> int:
        # self.hashset = set()
        self.count = len(s)

        for i in range(len(s)):
            # self.hashset.add(s[i])
            # print("odd", i)
            self.expand(i-1, i+1, s)
            # print("even", i)
            self.expand(i, i+1, s)

        return self.count
    
    def expand(self, l, r, s):
        # print(l, r)
        # if l >= 0 and r < len(s):
        #     print(s[l], s[r], s[l:r+1])
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1