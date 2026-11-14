'''
TOPOLOGICAL SORT (DFS + Cycle Detection)

Obiettivo: trovare un ordinamento dei corsi che rispetti tutti i prerequisites.

- visiting: nodi attualmente nel percorso DFS. Se incontro
  nuovamente un nodo presente qui, ho trovato un ciclo.
- visited: nodi già completati. Evita di riesplorarli.
- DFS esplora ricorsivamente tutti i prerequisites prima
  di completare il corso corrente.
- res.append(course): aggiunge il corso SOLO dopo aver
  completato tutte le sue dipendenze (Reverse Postorder).

Se trovo un ciclo, non esiste un ordinamento valido -> [].
Altrimenti, res contiene un ordinamento topologico valido.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
'''
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
                    # anche qua, altrimenti non aggiungo quelli senza pre
                    # che verrebberò aggiunti solo nella parte dopo!
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