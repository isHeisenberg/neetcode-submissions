class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #rows, cols = len(matrix) così ho solo un valore dato!
        n = len(matrix)
        
        # faccio trasposta
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # inverto rispetto a centro
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

        