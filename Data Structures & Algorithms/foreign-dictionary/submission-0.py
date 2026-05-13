class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []
        print(adj)
        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = True

            for nei in adj[node]:
                if dfs(nei):
                    return True
            
            visit[node] = False
            res.append(node)
        
        for c in adj:
            if dfs(c):
                return ""
                
        return "".join(res[::-1])