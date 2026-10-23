class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (0 <= r < rows and 0 <= c < cols
                    and grid[r][c] == INF):
                    grid[r][c] = dist + 1
                    queue.append((r, c, dist + 1))