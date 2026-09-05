class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prev in prerequisites:
            preMap[course].append(prev)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            # cycle check
            for prev in preMap[course]:
                if not dfs(prev):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        # cycle check 
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True