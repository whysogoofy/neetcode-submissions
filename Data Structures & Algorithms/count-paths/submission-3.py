class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        dp = {(n-1, m-1): 1}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == n or j == m:
                return 0

            paths_right = dfs(i+1, j)
            paths_down = dfs(i, j+1)

            total_paths = paths_right + paths_down

            dp[(i, j)] = total_paths
            
            return total_paths
        
        return dfs(0, 0)
