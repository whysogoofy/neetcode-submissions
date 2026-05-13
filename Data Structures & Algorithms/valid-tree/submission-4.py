class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            if edges:
                return False
            return True
        if len(edges) < n-1:
            return False

        adj = {i: [] for i in range(n)}
        visit, connected = set(), set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        # print(adj)
        
        def dfs(node, lastNode):
            if len(adj[node]) == 1 and adj[node] == lastNode:
                return True
            if node in visit or not adj[node]:
                return False

            visit.add(node)

            for neighbor in adj[node]:
                if neighbor != lastNode and not dfs(neighbor, node):
                    return False
            
            visit.remove(node)
            
            return True

        for node in adj:
            if not dfs(node, None):
                return False
            
        return True
            