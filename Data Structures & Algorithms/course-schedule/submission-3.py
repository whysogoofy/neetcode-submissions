class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the graph and track how many prerequisites each course has
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        # 2. Add all courses with NO prerequisites to the queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        finish_count = 0
        while queue:
            curr = queue.popleft()
            finish_count += 1
            
            # 3. "Take" the course and reduce indegree for its dependent courses
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                # If a neighbor has no more prerequisites, it's ready to be taken
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. If we finished all courses, there was no cycle
        return finish_count == numCourses