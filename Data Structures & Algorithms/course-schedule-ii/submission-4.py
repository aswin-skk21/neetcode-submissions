class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prev = defaultdict(list)
        visited = set()
        done = set()
        res = []

        for crs, pre in prerequisites:
            prev[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if course in done:
                return True
            
            visited.add(course)
            for pre in prev[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            done.add(course)
            res.append(course)
            prev[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res