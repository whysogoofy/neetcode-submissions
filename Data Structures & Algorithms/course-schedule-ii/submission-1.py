class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        output, visit = [], set()

        for course, pre in prerequisites:
            adj[course].append(pre)
        
        def dfs(course):
            if course in visit:
                return False
            if not adj[course]:
                if course not in output:
                    output.append(course)
                return True
            
            visit.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            if course not in output:
                output.append(course)
            visit.remove(course)
            adj[course] = []

            return True
        
        for course in adj:
            if not dfs(course):
                return []

        return output
