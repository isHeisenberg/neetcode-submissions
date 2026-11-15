'''
Circular Maximum Subarray (Kadane doppio).

- Kadane max: trova il sottoarray con somma massima (`globMax`).
- Kadane min: trova il sottoarray con somma minima (`globMin`).

In un array circolare, il sottoarray migliore può essere di due tipi:

- Normale: sta tutto in mezzo, senza attraversare il bordo. 
Esempio: [4].
- Che attraversa il bordo: prende un pezzo della fine e un pezzo dell'inizio. 
Esempio: in [5, -3, 5] il migliore è 5 + 5 = 10 (ultimo + primo).

Il caso 2 è furbo da calcolare: se prendi un pezzo dalla fine e uno dall'inizio, 
quello che lasci fuori è un blocco continuo in mezzo. Quindi:

somma del caso 2 = total - (blocco in mezzo che escludi)

Per renderla massima, devi escludere il blocco in mezzo con la somma più piccola. 
Cioè total - globMin.

Quindi servono due cose: il massimo sottoarray normale (globMax) 
e il minimo sottoarray normale (globMin).

Il best è il massimo tra:
  1. globMax: miglior sottoarray "in mezzo" (non attraversa il bordo)
  2. total - globMin: sottoarray che attraversa il bordo
     (totale meno il peggior blocco in mezzo)

Se sono tutti negativi (globMax <= 0) si ritorna globMax,
altrimenti total - globMin darebbe 0 (sottoarray vuoto, non valido).
Tempo O(n), spazio O(1).
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax