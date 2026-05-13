class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i+1: [] for i in range(len(edges))}
        visit, self.nodes = set(), []

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node, prev):
            if not adj[node]:
                return
            if node in visit:
                self.nodes.append([node, prev])
                return
            
            visit.add(node)

            for neighbor in adj[node]:
                if neighbor != prev:
                    dfs(neighbor, node)
            
            visit.remove(node)
        
        for node in adj:
            dfs(node, -1)
        
        res = []
        for node1, node2 in edges:
            for end1, end2 in self.nodes:
                # if (sorted([end1, end2])) == sorted([node1, node2]):
                #     res = [node1, node2]
                if [end1, end2] == [node1, node2]:
                    res = [node1, node2]
        
        return res