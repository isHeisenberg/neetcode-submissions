class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbours = defaultdict(list)
        for pr in prerequisites:
            neighbours[pr[0]].append(pr[1])

        # riguarda quelli percorsi nel dfs specifico
        visited = set()

        def dfs(i):
            if not neighbours[i]:
                return True
            if i in visited:
                return False

            visited.add(i)
            '''Non si può fare, 
            non posso modificare lista su cui itero
            rimuovo tutto alla fine'''
            # for neigh in neighbours[i]:
            #     if dfs(neigh):
            #         neighbours[i].remove(neigh)

            for neigh in neighbours[i]:
                if not dfs(neigh):
                    return False    # significa che c'è un loop dentro
            neighbours[i] = []
            #visited.remove(i)
            return True

        # lo runno da tutti i corsi perchè POTREBBE ESSERE SCONNESSO!
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        












