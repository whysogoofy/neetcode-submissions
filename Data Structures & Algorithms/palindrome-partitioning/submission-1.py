class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(comb):
            for i in range(len(comb)//2):
                if comb[i] != comb[len(comb) - i - 1]:
                    return False
            return True

        def dfs(i, part):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1, part)
                    part.pop()
            
        dfs(0, [])

        return res
