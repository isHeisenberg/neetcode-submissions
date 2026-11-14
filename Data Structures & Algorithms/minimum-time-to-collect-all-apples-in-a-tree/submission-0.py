'''
Tecnica: DFS ricorsiva post-order sul grafo non orientato (lista di adiacenza).
Si passa il genitore per non tornare indietro.

dfs(cur, par) restituisce il costo per raccogliere tutte le mele nel
sottoalbero di cur, partendo da cur e tornando a cur. Il time parte da 0
a ogni chiamata, perche ogni nodo ha il suo sottoalbero.

Per ogni figlio: se nel suo sottoalbero c'e almeno una mela
(childTime > 0 or hasApple[child]), si paga 2 + childTime, dove 2 e
l'andata e il ritorno sull'arco. Altrimenti il ramo viene ignorato.

Complessita: O(V + E) tempo, O(V + E) spazio.
'''
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)

        def dfs(cur, par):
            time = 0
            for child in adj[cur]:
                if child == par:
                    continue
                childTime = dfs(child, cur)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            return time

        return dfs(0, -1)


'''
SPACE COMPLEXITY IN RECURSION
Lo stack di ricorsione occupa O(h), dove h è l’altezza dell’albero (la profondità massima raggiunta da dfs). Ogni chiamata attiva tiene in memoria un frame con cur, par, time e l’iteratore del for.

Caso peggiore: albero a catena (ogni nodo ha un solo figlio), h = n, quindi O(n).
Caso migliore: albero bilanciato, h = log n, quindi O(log n).
'''