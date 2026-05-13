class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        output = ""
        count = {}
        curr_count = {}

        for char in t:
            count[char] = 1 + count.get(char, 0)

        have, need = 0, len(count)
        l = 0

        for r in range(len(s)):
            curr_count[s[r]] = 1 + curr_count.get(s[r], 0)
            have += 1 if count.get(s[r], 0) != 0 and curr_count[s[r]] == count[s[r]] else 0

            while have == need:
                if r - l + 1 < len(output) or output == "":
                    output = s[l:r+1]
                
                curr_count[s[l]] -= 1
                have -= 1 if count.get(s[l], 0) != 0 and curr_count[s[l]] < count[s[l]] else 0
                l += 1

        return output        