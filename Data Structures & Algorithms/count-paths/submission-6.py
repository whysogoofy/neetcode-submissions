from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
            
        # dp serves as both our cache and our visited set
        dp = {(n-1, m-1): 1}
        q = deque([(n-1, m-1)]) # Start right at the destination

        while q:
            i, j = q.popleft()

            if (i, j) != (n-1, m-1):
                dp_right = dp[(i+1, j)] if i+1 < n else 0
                dp_down = dp[(i, j+1)] if j+1 < m else 0
                dp[(i, j)] = dp_right + dp_down

            if i - 1 >= 0 and (i-1, j) not in dp:
                dp[(i-1, j)] = 0
                q.append((i-1, j))
                
            if j - 1 >= 0 and (i, j-1) not in dp:
                dp[(i, j-1)] = 0
                q.append((i, j-1))
        
        return dp[(0, 0)]