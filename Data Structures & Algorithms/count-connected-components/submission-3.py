class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        self.components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2: return
            union_root = root1 if rank[root1] > rank[root2] else root2
            parent[root1] = union_root
            parent[root2] = union_root
            rank[union_root] += 1
            self.components -= 1
        
        for edge in edges:
            node1, node2 = edge
            union(node1, node2)
            
        return self.components