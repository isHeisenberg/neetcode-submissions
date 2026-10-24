class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        time = 0

        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == 1):
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))

        return -1 if fresh > 0 else time















