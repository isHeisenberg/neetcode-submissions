'''
Kadane = a ogni posizione, scelgo se estendere il sottoarray precedente o
iniziarne uno nuovo,mantenendo il miglior risultato che termina qui.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            curr += nums[i]
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        
        return max_sum




'''
VERSIONE + CLEAN

5. Perché è Dynamic Programming?

Lo stato è:
dp[i] = massima somma di un sottoarray che finisce in i

La ricorrenza è:
dp[i]=\max(nums[i],dp[i-1]+nums[i])


def maxSubArray(nums):
    cur = nums[0]
    res = nums[0]

    for num in nums[1:]:
        cur = max(num, cur + num)
        res = max(res, cur)

    return res


Tempo: O(n), un solo passaggio.
Spazio: O(1), solo due variabili.
'''
