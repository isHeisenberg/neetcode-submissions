class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        max_area = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            area = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == 1 and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r, c)
                    max_area = max(max_area, area)

        return max_area



