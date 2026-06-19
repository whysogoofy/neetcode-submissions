class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = set()

        def stack_append(stack, ele):
            if not ele:
                return stack
            
            if stack and ele == ')':
                return stack-1
            
            return stack+1
            
        
        def dfs(i, stack):
            if i == len(s):
                return not stack
            if not stack and s[i] == ")" or (i, stack) in cache:
                return False

            if s[i] != '*':
                return dfs(i+1, stack_append(stack, s[i]))
            
            vals = ['(', ')', '']

            for val in vals:
                if dfs(i+1, stack_append(stack, val)):
                    return True
            
            cache.add((i, stack))
            return False
        
        return dfs(0, 0)
                