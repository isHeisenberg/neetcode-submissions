class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = collections.deque()
        
        # we put all the treasures in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            row, col = q.popleft()
            #visited.add((row, col)) stai facendo due volte così!
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 2147483647 and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
                    grid[r][c] = grid[row][col] + 1

                    
    




