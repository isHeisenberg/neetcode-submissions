class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        for i in range(l):
            for j in range(l):
                if (board[i][j] == '.'):
                    continue # va al prossimo ciclo su "j"
                for c in range(j+1, l):
                    if (board[i][j] == board[i][c]):
                        return False

        for i in range(l):
            for j in range(l):
                if (board[j][i] == '.'):
                    continue
                for c in range(j+1, l):
                    if (board[j][i] == board[c][i]):
                        return False

        # for i in range(0, l, 3):
        #     for j in range(0, l, 3):
        #         if (board[i][j] == '.'):
        #             continue
        #         for c in range(i+1, i+3):
        #             for d in range(j+1, j+3):
        #                 if (board[i][j] == board[c][d]):
        #                     return False

        # 🔹 Controllo box 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        if board[box_row + i][box_col + j] == ".":
                            continue
                        for x in range(3):
                            for y in range(3):
                                if (i, j) != (x, y):
                                    if board[box_row + i][box_col + j] == board[box_row + x][box_col + y]:
                                        return False

        
        return True




