class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        dp = {(n-1, m-1): 1}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == n or j == m:
                return 0

            total_paths = dfs(i+1, j) + dfs(i, j+1)

            dp[(i, j)] = total_paths
            
            return total_paths
        
        return dfs(0, 0)
