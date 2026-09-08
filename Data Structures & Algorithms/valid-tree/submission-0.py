class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        # mi serve avere anche parent, infatti essendo undirected
        # se facessi neighbor avrei uno già visto sempre e troverebbe falsi positivi
        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:  
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        # Controllo cicli: parto da 0 e controllo tutto il grafo
        if not dfs(0, -1):
            return False

        # Controllo che tutti i nodi siano collegati (cioè se visitati tutti con unico DFS)
        return len(visited) == n





