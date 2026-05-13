class Solution:
    def climbStairs(self, n: int) -> int:
        dp_map = {}

        def dfs(steps):
            if steps >= n:
                return 0
            if steps == n - 1:
                return 1
            if steps == n - 2:
                return 2
            if steps in dp_map:
                return dp_map[steps]
            
            res = dfs(steps+1) + dfs(steps+2)
            dp_map[steps] = res

            return res

        return dfs(0)