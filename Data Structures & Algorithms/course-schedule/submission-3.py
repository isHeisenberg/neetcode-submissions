class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = collections.defaultdict(list)
        for p in prerequisites: 
            preMap[p[0]].append(p[1])

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False    # Cycle detected
            if preMap[crs] == []:
                return True     # No prerequisites

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True




