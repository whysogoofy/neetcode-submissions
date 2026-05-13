class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) == 1: return False
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack:
                    return False
                elif opening.index(stack[-1]) == closing.index(char):
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False