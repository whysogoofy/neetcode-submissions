class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""

        for char in s:
            if char.isalnum():
                alnum_s += char
        
        if len(alnum_s) == 1 or len(alnum_s) == 0:
            return True

        mid = len(alnum_s) // 2


        for i in range(mid + 1):
            if alnum_s[i].lower() != alnum_s[len(alnum_s) - i -1].lower():
                return False

        return True 