'''
RICORDA DI SALTARE I DOPPIONI

ESEMPIO: nums = [1, 2, 2, 3, 4, 5]

Fissiamo i = 0 -> nums[i] = 1.

Primo tentativo: j = 1 -> nums[j] = 2
    [1, 2, _, _, _, _]

    I two pointers cercano tutte le coppie successive:
    [2, 3, 4, 5]

    Possono trovare:
    [1, 2, 2, 5]
    [1, 2, 3, 4]

Secondo tentativo: j = 2 -> nums[j] = 2
    [1, _, 2, _, _, _]

    Non serve riprovare!
    [1, 2, 2, 5] l'avevo già trovato, non perdo nulla
    Con j = 1 abbiamo già provato tutte le combinazioni
    che iniziano con [1, 2].

IMPORTANTE:
- Il secondo 2 NON viene eliminato dalla quadrupla.
- Quando j = 1, i two pointers possono comunque usarlo!
- Saltiamo il duplicato solo come scelta di j,
  non come numero utilizzabile nella quadrupla.

Quindi evitiamo quadruple duplicate senza perdere soluzioni.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        # -4 -3 -2 -1
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # two pointers
                l, r = j+1, n-1
                while l < r:
                    somma = nums[i] + nums[j] + nums[l] + nums[r]
                    if somma == target:
                        lista = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(lista)
                        vecchio_l = l
                        # IMPORTANTE: itero finchè num diversi da quelli che ho
                        while l < r and nums[l] == nums[vecchio_l]:
                            l += 1                         
                    if somma < target:
                        l += 1
                    else:
                        r -= 1

        return res
