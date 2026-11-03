'''
DUPLICATI IN 3SUM:

Esempio: nums = [-2, 0, 0, 2, 2]

Trovo la tripletta:
[-2, 0, 2]

Dopo averla salvata:
- Salto gli eventuali duplicati di l (altri 0).
- Salto gli eventuali duplicati di r (altri 2).

Perché?
Spostandomi su valori uguali, otterrei nuovamente
la stessa tripletta [-2, 0, 2].

IMPORTANTE:
I duplicati non vengono eliminati dall'array.
Evito solo di generare risultati ripetuti.
SALTA SIA DA DESTRA CHE DA SINISTRA
E SALTA ANCHE SU INDICE i, DATO CHE HO GIà PRESO LA TRIPLETTA PRIMA
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            # Evito di riprovare lo stesso primo numero
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1

            while l < r:
                somma = nums[i] + nums[l] + nums[r]

                if somma == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Salto i duplicati di l
                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    # Salto i duplicati di r
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif somma < 0:
                    l += 1
                else:
                    r -= 1

        return res

