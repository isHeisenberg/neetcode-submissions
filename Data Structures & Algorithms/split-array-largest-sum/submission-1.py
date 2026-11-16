'''
L'idea: invece di cercare come dividere l'array, si ipotizza la risposta 
(la somma massima consentita per un sottoarray) e si verifica se è realizzabile.

canSplit(dim) è un controllo greedy: si può tagliare l'array in al massimo k pezzi, 
in modo che nessun pezzo abbia somma maggiore di dim? Si aggiungono i numeri al pezzo
corrente e, quando la somma supererebbe dim, si inizia un nuovo pezzo con il numero
corrente. counter conta i tagli, quindi il numero di pezzi è counter + 1.
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(dim):
            somma = 0
            counter = 0
            for n in nums:
                somma += n
                if somma > dim:
                    counter += 1
                    somma = n

            return counter + 1 <= k
        
        l, r = max(nums), sum(nums)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res