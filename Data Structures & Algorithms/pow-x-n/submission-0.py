class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)
        
        cache = {}

        def dfs(exp):
            if exp == 0:
                return 1
            rem = exp % 2
            half = exp // 2

            if half in cache:
                cache[exp] = (x ** rem) * (cache[half] ** 2)
            else:
                cache[exp] = (x ** rem) * (dfs(half) ** 2)
            
            return cache[exp]
        
        return dfs(n)
