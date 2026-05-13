class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            part = str(len(s)) + "#" + s
            output += part

        return output

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
            
        i = 0
        output = []

        curr_num = ""
        while s[i] != "#":
            curr_num += s[i]
            i += 1
        i += 1
        curr_end = i + int(curr_num)

        curr_word = ""
        while i < len(s) + 1:
            if i < curr_end:
                curr_word += s[i]
                i += 1
            else:
                output.append(curr_word)
                if i == len(s):
                    break
                curr_word = ""
                curr_num = ""
                while s[i] != "#":
                    
                    curr_num += s[i]
                    i += 1
                
                i += 1
                curr_end = i + int(curr_num)
                
                


                
        return output