# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # considero il target positivo (è la stessa cosa)
#         # btw tutti i nums sono positivi, no check
#         target = abs(target)

#         # dp[i]: in quanti modi riesco a fare i
#         dp = [0] * (target + 1)
#         dp[0] = 1

#         # 0/1 KNAPSACK
#         # Quindi vado da fine a inizio
#         for num in nums:
#             for i in range(target, num - 1, -1):
#                 # da checkare
#                 if i + num in range(target+1):
#                     dp[i] = dp[i] + dp[i + num]
#                 if i - num in range(target+1):
#                     dp[i] = dp[i] + dp[i - num]

#         return dp[target]



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Impossibile raggiungere target
        if abs(target) > total:
            return 0

        # Trasformazione in subset sum
        if (total + target) % 2:
            return 0

        target = (total + target) // 2

        # dp[i] = modi per ottenere la somma i
        dp = [0] * (target + 1)
        dp[0] = 1

        # 0/1 Knapsack: ogni numero si usa al massimo una volta
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target]







