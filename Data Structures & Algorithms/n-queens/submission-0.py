
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        matrice = [['.'] * n for _ in range(n)]
        result = []

        # non serve controllare riga, pk sicuro metto una Q per riga
        def safe(row, col):
            for r in range(row):
                # Stessa colonna
                if matrice[r][col] == 'Q':
                    return False
                # MOLTO UTILE PER DIAGONALI (r1,c1) (r2,c2):
                # Stessa diagonale sse: |r_1-r_2| = |c_1-c_2|
                # Infatti stessa distanza verticale e orizzontale!
                if abs(row - r) == abs(col - next(
                    c for c in range(n) if matrice[r][c] == 'Q')):
                    return False
            return True

        def backtrack(row):
            # Tutte le righe hanno una regina
            if row == n:
                result.append([''.join(r) for r in matrice])
                return

            for col in range(n):
                if safe(row, col):
                    # Scelta
                    matrice[row][col] = 'Q'
                    # Esplora
                    backtrack(row + 1)
                    # Undo e provo con prossimo col
                    # Non serve richiamare backtrack, pk c'è già il for!
                    matrice[row][col] = '.'

        backtrack(0)

        return result




