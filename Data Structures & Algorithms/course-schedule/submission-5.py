class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()
        finished = 0

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        print(preMap)
        
        def dfs(course):
            if not preMap[course]:
                return True
            if course in visit:
                print(course)
                return False

            isPossible = True
            visit.add(course)

            for pre in preMap[course]:
                isPossible = isPossible and dfs(pre)
                
            visit.remove(course)
            
            return isPossible

        for course in preMap:
            print("dfs", course)
            if dfs(course):
                finished += 1
            visit = set()
        
        return finished == numCourses