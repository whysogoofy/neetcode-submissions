class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max_len = 0
        i = 0

        while i < len(s) - 1:
            hashmap = {}
            output = s[i]
            hashmap[s[i]] = 1
            for k in range(i + 1, len(s)):
                char = s[k]
                freq = hashmap.get(char, 0)
                if freq == 0:
                    output += char
                    hashmap[char] = 1
                elif freq == 1:
                    # print(output)
                    break

            # print(output, max_len)
            max_len = max(max_len, len(output))
            i += 1
            
        return max_len
        