'''
Grafo diretto: conteggio dei gradi dei nodi.

- In-degree: quante persone si fidano di lui.
- Out-degree: quante persone lui considera affidabili.
- Il giudice ha in-degree = n-1 e out-degree = 0.

Non serve DFS/BFS: basta contare gli archi.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for i,j in trust:
            indegree[j] += 1
            outdegree[i] += 1
        
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1