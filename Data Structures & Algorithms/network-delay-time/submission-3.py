class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # passo a una adj list
        edges = defaultdict(list)
        # { a: [(b, 3), (c, 2)] }
        for time in times:
            edges[time[0]].append((time[1], time[2]))
        

        minHeap = [(0, k)]  # per sapere sempre chi è il minimo: (dist, nodo)
        visit = set()       # per non finire in un ciclo
        t = 0               # per risultato, ci metto valore massimo finale

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit: # non voglio rivisitare lo stesso nodo
                continue
            
            visit.add(n1)
            t = max(t, w1)
            # faccio BFS
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2))  # total path come distanza
            
        return t if len(visit) == n else -1 # ricorda il check se presi tutti!

# complessità O(E * logV)




