class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        # (effort, r, c)
        heap = [(0, 0, 0)]
        visited = set()

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        while heap:
            effort, r, c = heapq.heappop(heap)
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
