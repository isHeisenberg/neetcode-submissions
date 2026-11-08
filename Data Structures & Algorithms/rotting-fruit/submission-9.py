'''
Multi-source BFS.

Quando hai più punti di partenza e vuoi che la BFS si espanda contemporaneamente da tutti, inserisci tutte le sorgenti iniziali nella queue prima di avviare il while.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        time = 0

        # inserisco tutte le sorgenti all'inizio!
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                
        while q:
            row, col, t = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                    grid[r][c] = 2
                    q.append((r, c, t+1))
                    time = t + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time

        
        








