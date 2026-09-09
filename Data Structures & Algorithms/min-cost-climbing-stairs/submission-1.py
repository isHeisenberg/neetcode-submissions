class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i]: costo minimo per raggiungere il gradino i
        dp = [0] * (n + 1)

        # costo minimo per raggiungere i-1 + costo gradino i-1 per muovermi
        # same per i-2
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]