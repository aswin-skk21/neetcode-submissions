class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prev = defaultdict(list)
        visited = set()

        for crs, pre in prerequisites:
            prev[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if course not in prev or prev[course] == []:
                return True
            
            visited.add(course)
            for pre in prev[course]:
                if not dfs(pre):
                    return False 
            visited.remove(course)
            prev[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True