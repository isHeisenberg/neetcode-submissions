class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        # dp[x]: minimo numero di monete per fare x
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], 1 + dp[x-c])
        
        return dp[-1] if dp[-1] != INF else -1
            
