class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        

        def bfs(r, c):
            q = collections.deque()
            area = 0
            # faccio a mano aggiunta del primo elemento che ho sia in q che visit
            visited.add((r, c))
            q.append((r, c))

            while q:    
                row, col = q.popleft()  # ricorda che è una queue: faccio popleft()
                area += 1
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and
                        (r, c) not in visited and grid[r][c] == 1):
                        q.append((r, c))
                        visited.add((r, c))
 
            return area


        if not grid:
            return 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))
                    visited.add((r,c))
        
        return maxArea
