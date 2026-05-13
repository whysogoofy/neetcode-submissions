class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = {}
        res = 0

        l = 0
        for r in range(len(s)):
            char_set[s[r]] = 1 + char_set.get(s[r], 0)

            while r - l + 1 - max(char_set.values()) > k:
                char_set[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
            
            

            