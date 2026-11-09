from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        q = deque()

        # Multi-source BFS: parto da tutti i treasure
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r+dr, c+dc

                if (0 <= row < rows and
                    0 <= col < cols and
                    grid[row][col] == INF):

                    grid[row][col] = grid[r][c] + 1
                    q.append((row, col))