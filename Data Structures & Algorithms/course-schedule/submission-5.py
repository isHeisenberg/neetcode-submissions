class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

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




'''
VERSIONE SE AVESSI AVUTO UNA MATRICE DI ADIACENZA IN INPUT
- Posso modificare i valori in tabella, comodo

def canFinish(m):
    n = len(m)
    state = [0] * n  # 0 = non visitato, 1 = in corso, 2 = completato

    def dfs(i):
        if state[i] == 1:
            return False      # trovato un ciclo
        if state[i] == 2:
            return True       # già verificato
        state[i] = 1
        for j in range(n):
            if m[i][j] == 1:
                if not dfs(j):
                    return False
        state[i] = 2
        return True

    for i in range(n):
        if not dfs(i):
            return False
    return True
'''













