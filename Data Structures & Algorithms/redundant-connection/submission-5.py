'''
TECNICA: cycle detection con DFS su grafo non orientato, poi ricostruzione
del ciclo durante il ritorno della ricorsione.

OBIETTIVO
Il grafo è un albero con un arco in più, quindi ha esattamente un ciclo.
Bisogna ritornare l'ultimo arco dell'input che fa parte di quel ciclo.

LOGICA STEP BY STEP

1. Costruisco la lista di adiacenza.
   Ogni arco [u, v] viene aggiunto in entrambe le direzioni, perché il
   grafo è non orientato. Uso n + 1 posti perché i nodi vanno da 1 a n.

2. Avvio la DFS dal nodo 1.
   Basta una sola partenza perché il grafo è connesso. Passo anche il
   parent (il nodo da cui arrivo), all'inizio -1.

3. Rilevo il ciclo.
   Se entro in un nodo già visitato, ho chiuso un ciclo. Questo nodo è
   l'inizio del ciclo: lo salvo in cycleStart e ritorno True.
   Il parent viene saltato nel ciclo for, altrimenti l'arco appena
   percorso, visto dall'altro lato, sembrerebbe un ciclo falso.

4. Propago il True verso l'alto.
   Quando una chiamata ritorna True, la ricorsione sta risalendo lungo il
   percorso che ha portato al ciclo. Il return True ferma anche la DFS,
   senza esplorare altri vicini.

5. Raccolgo i nodi del ciclo durante la risalita.
   Finché cycleStart è diverso da -1, ogni nodo che risale è sul ciclo,
   quindi lo aggiungo a cycle.

6. Fermo la raccolta quando il ciclo è completo.
   Quando risalendo arrivo al nodo uguale a cycleStart, il ciclo è chiuso.
   Questo nodo viene aggiunto (l'if di aggiunta sta prima del reset) e poi
   metto cycleStart = -1. I nodi sopra, che stanno sul gambo che porta al
   ciclo ma non nel ciclo, non vengono aggiunti.

7. Trovo la risposta.
   Scorro gli archi dall'ultimo al primo. Il primo con entrambi gli
   estremi in cycle è l'arco cercato. Basta controllare i nodi, perché
   con un solo ciclo nessun arco extra può unire due nodi del ciclo.

ESEMPIO
edges = [[1,2],[2,3],[3,1]]
dfs(1) va a 2, poi a 3, poi chiama dfs(1) già visitato, quindi
cycleStart = 1 e ritorna True. Risalendo si aggiungono 3, 2, 1 e al nodo 1
si resetta cycleStart. cycle = {1, 2, 3}. Scorrendo al contrario il primo
arco valido è [3, 1].

COMPLESSITÀ
Tempo O(n), spazio O(n).
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []


