'''
TECNICA: Topological Sort (Kahn's Algorithm) + BFS

IDEA:
- Ogni carattere è un nodo del grafo.
- Se un carattere deve precederne un altro, creo un arco.
  Es: "wrt" e "wrf" -> t prima di f -> t -> f.
- Indegree = numero di archi entranti (prerequisiti).
- Parto dai nodi con indegree 0 e li elaboro con BFS.

CONCETTI RIUTILIZZABILI:
- Topological Sort: ordina nodi rispettando le dipendenze.
- Kahn's Algorithm: BFS basata sugli indegree.
- Cycle detection: se non elaboro tutti i nodi, c'è un ciclo.
- Set negli adjacency list: evita archi duplicati.
- Un nodo può essere aggiunto alla queue quando tutti
  i suoi prerequisiti sono stati soddisfatti (indegree == 0).

COMPLESSITA':
V = numero di caratteri distinti
E = numero di relazioni tra caratteri
Tempo: O(V + E) + costo confronto parole
Spazio: O(V + E)
'''

class Solution:
    def foreignDictionary(self, words):
        # Ogni carattere è un nodo, inizialmente senza archi
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        # Ricavo le relazioni confrontando parole consecutive
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Caso invalido: "abc" prima di "ab"
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # La prima lettera diversa determina l'ordine
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # Evito archi duplicati e indegree errati
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # Parto dai nodi senza prerequisiti
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        # Kahn's Algorithm: BFS
        while q:
            char = q.popleft()
            res.append(char)

            # Rimuovo virtualmente gli archi uscenti
            for neighbor in adj[char]:
                indegree[neighbor] -= 1

                # Tutti i prerequisiti sono soddisfatti
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Se mancano nodi, esiste un ciclo (ordine impossibile)
        if len(res) != len(indegree):
            return ""

        return "".join(res)








        