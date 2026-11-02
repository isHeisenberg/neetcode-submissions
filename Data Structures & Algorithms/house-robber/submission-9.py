class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # dp[i]: massimo rubabile nelle case da 0 a i
        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            a, b = b, max(nums[i] + a, b)

        return b


'''
Qua con n+1, tiene uno spazio aggiuntivo all'inizio
Così nel caso array fosse lungo 1, nel for non scoppia
Perchè ho quel dp[0] in cui ho zero
ATTENZIONE però, perchè devo allora shiftare gli indici di -1 per essere coerente con nums

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]: massimo rubabile considerando le prime i case
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[n]
'''