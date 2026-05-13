class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()
        finished = 0

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # print(preMap)
        
        def dfs(course):
            if not preMap[course]:
                return True
            if course in visit:
                print(course)
                return False

            isPossible = True
            visit.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
                
            visit.remove(course)
            preMap[course] = []
            return True

        for course in preMap:
            if not dfs(course):
                return False
        
        return True