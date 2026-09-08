class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None

        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # ci metto tutte le celle dei bordi che voglio visitare
        borders = []

        for c in range(cols):
            borders.append((0, c))        # prima riga
            borders.append((rows - 1, c)) # ultima riga

        for r in range(1, rows-1):
            borders.append((r, 0))        # prima colonna
            borders.append((r, cols - 1)) # ultima colonna

        visited = set()

        def bfs(start_r, start_c):
            q = collections.deque()
            
            if board[start_r][start_c] == "O":
                q.append((start_r, start_c))
                visited.add((start_r, start_c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and board[r][c] == "O" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))


        # qui vado a definire tutti i visitati dai bordi
        for r, c in borders:
            bfs(r, c)

        # tutto ciò che non è visitato lo pongo a "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"


        

        