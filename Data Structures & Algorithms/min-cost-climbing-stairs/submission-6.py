class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[x]: minimo costo per raggiungere x
        dp = [0] * (n+1)
        
        '''
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        “costo per arrivare al gradino da cui parto + costo per ripartire da lì”.
        '''
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        
        return dp[-1]



    