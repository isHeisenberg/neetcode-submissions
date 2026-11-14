class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            if not preMap[course]:
                if course not in visited:
                    res.append(course)
                    visited.add(course)
                return True

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            preMap[course] = []
            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True


        for c in range(numCourses):
            if not dfs(c):
                return []

        return res