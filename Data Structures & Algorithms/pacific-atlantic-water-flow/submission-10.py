class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        atlantic = [[False] * len(heights[0]) for _ in range(len(heights))]

        p_queue = deque()
        a_queue = deque()

        # prima riga e prima colonna per pacifico
        for i in range(cols):
            p_queue.append((0, i))
            pacific[0][i] = True
        for j in range(rows):
            p_queue.append((j, 0))
            pacific[j][0] = True

        # ultima riga e ultima colonna per atlantico
        for i in range(cols):
            a_queue.append((rows-1, i))
            atlantic[rows-1][i] = True
        for j in range(rows):
            a_queue.append((j, cols-1))
            atlantic[j][cols-1] = True


        def bfs(queue, ocean):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and 
                        ocean[row][col] == False and heights[r][c] <= heights[row][col]):
                        queue.append((row, col))
                        ocean[row][col] = True
        
        bfs(p_queue, pacific)
        bfs(a_queue, atlantic)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res
                    














