class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        path = ["JFK"]

        for u, v in tickets:
            adj[u].append(v)
            adj[u].sort()
        # print(adj)
        
        def dfs(node):
            # print("dfs", node, adj)
            if len(path) == len(tickets) + 1:
                return True
            if node not in adj:
                return False 

            neighbors = list(adj[node])
            for i, neighbor in enumerate(neighbors):
                adj[node].pop(i)
                path.append(neighbor)

                if dfs(neighbor):
                    return True
                
                adj[node].insert(i, neighbor)
                path.pop()

            return False

        
        dfs("JFK")

        return path
            
