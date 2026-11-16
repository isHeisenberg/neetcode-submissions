'''
Vogliamo sapere:

- qual è il massimo prodotto di un subarray che FINISCE in i?
- qual è il minimo prodotto di un subarray che FINISCE in i?

Perché anche il minimo ci interessa?
Perché un numero negativo può trasformare il minimo precedente nel massimo attuale.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = 1
        minprod = 1
        res = nums[0]

        for num in nums:
            temp = maxprod*num
            maxprod = max(temp, minprod*num, num)
            minprod = min(temp, minprod*num, num)
            res = max(res, maxprod)

        return res

















