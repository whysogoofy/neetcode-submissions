class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {}
        digit_map["2"] = "abc"
        digit_map["3"] = "def"
        digit_map["4"] = "ghi"
        digit_map["5"] = "jkl"
        digit_map["6"] = "mno"
        digit_map["7"] = "pqrs"
        digit_map["8"] = "tuv"
        digit_map["9"] = "wxyz"

        arr = list(digits)
        output = []

        def dfs(i, substring):
            if i == len(digits):
                if substring: output.append("".join(substring))
                return
            
            for char in digit_map[digits[i]]:
                substring.append(char)
                dfs(i+1, substring)
                substring.pop()
            
        dfs(0, [])
        return output