class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]: in quanti modi posso arrivarci dalla fine
        # cella di arrivo metto solo 1
        dp = [ [0] * n for _ in range(m) ]
        dp[-1][-1] = 1
        # prendo da sotto e da dx
        directions = [[0, 1], [1, 0]]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                for rd, rc in directions:
                    if r + rd in range(m) and c + rc in range(n):
                        dp[r][c] += dp[r+rd][c+rc]

        return dp[0][0]