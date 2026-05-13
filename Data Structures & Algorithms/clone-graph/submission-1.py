"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = {}
        
        def dfs(root):
            if root in visit:
                return
            
            visit[root] = Node(root.val)
            
            for neighbor in root.neighbors:
                dfs(neighbor)
                visit[root].neighbors.append(visit[neighbor])
        
        dfs(node)

        return visit[node]



        