class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        # multi-source BFS, metto tutti i punti di partenza
        # ricorda di scrivere DEQUE()!
        pacific = deque()
        atlantic = deque()

        pacific_visited = [ [False] * cols for _ in range(rows) ]
        atlantic_visited = [ [False] * cols for _ in range(rows) ]

        for i in range(rows):
            pacific.append((i, 0))
            atlantic.append((i, cols-1))
            pacific_visited[i][0] = True
            atlantic_visited[i][cols-1] = True

        for j in range(cols):
            pacific.append((0, j))
            atlantic.append((rows-1, j))
            pacific_visited[0][j] = True
            atlantic_visited[rows-1][j] = True

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row in range(rows) and 
                    col in range(cols) and 
                    not visited[row][col] and 
                    heights[r][c] <= heights[row][col]):
                        visited[row][col] = True
                        queue.append((row, col))

        bfs(pacific, pacific_visited)
        bfs(atlantic, atlantic_visited)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pacific_visited[r][c] and atlantic_visited[r][c]:
                    res.append([r,c])

        return res



















