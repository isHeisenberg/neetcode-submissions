'''
You must design an algorithm where sumRegion works on O(1) time complexity.

Necessariamente un DP problem
dp[i][j] = 
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0]) 
        self.dp = [ [0] * cols for _ in range(rows) ]

        for r in range(rows):
            for c in range(cols):
                somma = self.matrix[r][c]

                # sommo sopra
                # if r-1 in range(rows): più clean con r>0
                if r > 0: 
                    somma += self.dp[r-1][c]

                # sommo sinistra
                if c > 0:
                    somma += self.dp[r][c-1]

                # sottraggo parte che overlappa
                if r > 0 and c > 0:
                    somma -= self.dp[r-1][c-1]

                self.dp[r][c] = somma


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.dp[row2][col2]

        if row1 > 0:
            res -= self.dp[row1-1][col2]
        if col1 > 0:
            res -= self.dp[row2][col1-1]

        # altrimenti rimuovo due volte la parte in comune!
        if row1 > 0 and col1 > 0:
            res += self.dp[row1-1][col1-1]

        return res







# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)