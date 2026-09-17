class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            perimeter = 0

            while q: 
                ri, ci = q.popleft()
                free_edges = 4
                for dr, dc in directions:
                    row, col = ri + dr, ci + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        free_edges -= 1
                        if (row, col) not in visited:
                            q.append((row, col))
                            visited.add((row, col))
                
                perimeter += free_edges

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)

        return 0

