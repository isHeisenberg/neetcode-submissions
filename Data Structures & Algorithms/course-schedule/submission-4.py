from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Grafo: prerequisito -> corsi che dipendono da lui
        graph = defaultdict(list)
        # Quanti prerequisiti restano da completare per ogni corso
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Parti dai corsi senza prerequisiti
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        completed = 0

        while queue:
            crs = queue.popleft()
            completed += 1
            for nxt in graph[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # Se ne abbiamo completati tutti, nessun ciclo
        return completed == numCourses








