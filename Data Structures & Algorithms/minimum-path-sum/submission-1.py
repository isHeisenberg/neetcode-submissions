class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Base Cases
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]               # partenza
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]  # prima riga
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]  # prima colonna
                # General Case
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]  

        return dp[m-1][n-1]