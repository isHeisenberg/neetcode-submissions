class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()

        for i in range(cols):
            if board[0][i] == "O":
                board[0][i] = "A"
                queue.append((0, i))

            if board[rows-1][i] == "O":
                board[rows-1][i] = "A"
                queue.append((rows-1, i))
            
        for j in range(rows):
            if board[j][0] == "O":
                board[j][0] = "A"
                queue.append((j, 0))

            if board[j][cols - 1] == "O":
                board[j][cols - 1] = "A"
                queue.append((j, cols - 1))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "A"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "A":
                    board[r][c] = "O"

        

        