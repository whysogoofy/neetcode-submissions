class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = set()

        def stack_append(stack, ele):
            if not ele:
                return
            if not stack:
                stack.append(ele)
                return
            
            if stack[-1] == '(' and ele == ')':
                stack.pop()
                return
            
            stack.append(ele)
            
        
        def dfs(i, stack):
            if i == len(s):
                return not len(stack)
            if (i, tuple(stack)) in cache:
                return False

            if s[i] != '*':
                stack_append(stack, s[i])
                return dfs(i+1, stack)
            
            vals = ['(', ')', '']

            for val in vals:
                stack_cp = stack.copy()
                stack_append(stack_cp, val)
                if dfs(i+1, stack_cp):
                    return True
            
            cache.add((i, tuple(stack)))
            return False
        
        return dfs(0, [])
                