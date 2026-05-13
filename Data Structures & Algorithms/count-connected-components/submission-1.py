class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visit, output = set(), 0

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        for node in adj:
            if not adj[node]:
                output += 1
        
        def dfs(node):
            if not adj[node] or node in visit:
                return
            
            visit.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
            
            visit.remove(node)
            adj[node] = []
        
        for node in adj:
            if adj[node]:
                output += 1
                dfs(node)

        return output