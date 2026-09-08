class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1->2 2->3 3->1 se trovo un ciclo allora non è possibile -> False
        adj = collections.defaultdict(list)
        for p in prerequisites: 
            adj[p[0]].append(p[1])

        # nodi che sono nel path attivo della ricorsione. Se li rincontro, è un ciclo
        visited = set()
        # nodi che ho già esplorato completamente e so per certo che non portano a nessun ciclo
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False  # ciclo trovato
            if course in visited:
                return True   # già esplorato, nessun ciclo da qui

            visiting.add(course)
            for neighbor in adj[course]: # così vado sui edges che partono dal nodo (itero su lista dict)
                if not dfs(neighbor):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        # per ogni corso vedo se si può fare
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True



