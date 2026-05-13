class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        elif len(s) < len(t):
            return ""

        output = ""
        count = {}

        for char in t:
            count[char] = 1 + count.get(char, 0)

        i, j = 0, 0

        while j < len(s):
            if count.get(s[i], 0) == 0:
                i += 1
                j += 1
            else:
                print(i, j, s[i], s[j])
                curr_count = {}
                while j < len(s) and curr_count != count:
                    if count.get(s[j], 0) != 0 and curr_count.get(s[j], 0) < count.get(s[j], 0):
                        curr_count[s[j]] = 1 + curr_count.get(s[j], 0)
                    j += 1
                # print(count, curr_count)
                if curr_count == count:
                    # print("case match", output, s[i:j], i, j, len(output))
                    if  j - i < len(output) or output == "":
                        output = s[i:j]
                i += 1
                j = i
        
        return output


        