'''
Dijkstra with Min Heap:
- Parto dalla cella (0,0) con effort 0.
- La heap estrae sempre la cella con effort minimo.
- Il nuovo effort è il massimo tra quello corrente e la differenza di altezza tra le due celle.
- Uso dist per memorizzare il minimo effort conosciuto per raggiungere ogni cella.
- Aggiorno e inserisco nella heap solo se trovo un effort migliore.
- Quando estraggo la cella finale, ho trovato il minimo effort possibile.

Time Complexity: O(R * C * log(R * C))
Space Complexity: O(R * C)

R = numero di righe, C = numero di colonne.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        # (effort, r, c)
        heap = [(0, 0, 0)]
        visited = set()

        # ottimizzazione per salvarmi il miglior effort finora
        # così evito di ripartire da punti inutili
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            if r == rows-1 and c == cols-1:
                return effort
            
            visited.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row in range(rows) and 
                col in range(cols) and 
                (row, col) not in visited):
                    eff = max(effort, abs(heights[r][c] - heights[row][col]))
                    if eff < dist[row][col]:
                        dist[row][col] = eff
                        heapq.heappush(heap, (eff, row, col))




