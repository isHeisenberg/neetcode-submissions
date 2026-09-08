class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []

        def bfs(start_r, start_c):
            q = collections.deque()
            q.append((start_r, start_c))
            visited = set()
            pacific = False
            atlantic = False

            if start_r == 0 or start_c == 0:
                pacific = True
            if start_r == rows-1 or start_c == cols-1:
                atlantic = True

            if pacific and atlantic:
                res.append([start_r, start_c])
                return
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and heights[r][c] <= heights[row][col] and (r, c) not in visited:
                        if r == 0 or c == 0:
                            pacific = True
                        if r == rows-1 or c == cols-1:
                            atlantic = True

                        if pacific and atlantic:
                            res.append([start_r, start_c])
                            return
                        
                        q.append((r, c))
                        visited.add((r,c))
                    

        for r in range(rows):
            for c in range(cols):
                bfs(r, c)
        
        return res




