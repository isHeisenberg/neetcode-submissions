class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * cols
        dp[-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < cols:
                    dp[c] += dp[c+1]

        return dp[0]


'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j] = possibili percorsi partendo da ij
        dp = [ [0] * cols for _ in range(rows) ]
        dp[-1][-1] = 1
        directions = [ [0, 1], [1, 0]]

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    for dr, dc in directions:
                        if (r + dr) in range(rows) and (c + dc) in range(cols):
                            dp[r][c] += dp[r + dr][c + dc]
        
        return dp[0][0]
'''