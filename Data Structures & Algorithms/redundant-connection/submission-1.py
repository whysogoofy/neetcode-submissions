class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        rank = [1 for _ in range(len(edges))]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return 1
            
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            
            return 0

        for node1, node2 in edges:
            if union(node1-1, node2-1):
                return [node1, node2]