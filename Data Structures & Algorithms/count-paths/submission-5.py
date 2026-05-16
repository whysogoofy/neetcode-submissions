class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        q, dp, visit = deque([(n-2, m-1), (n-1, m-2)]), {(n-1, m-1): 1}, set([(n-2, m-1), (n-1, m-2)])

        while q:
            for i in range(len(q)):
                i, j = q.popleft()

                dp_right = dp[(i+1, j)] if i+1 < n else 0
                dp_down = dp[(i, j+1)] if j+1 < m else 0
                dp[(i, j)] = dp_right + dp_down

                if i-1 >= 0 and (i-1, j) not in visit:
                    visit.add((i-1, j))
                    q.append((i-1, j))
                if j-1 >= 0 and (i, j-1) not in visit:
                    visit.add((i, j-1))
                    q.append((i, j-1))
        
        return dp[(0, 0)]
