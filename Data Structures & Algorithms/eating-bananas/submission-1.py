class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        # pile // k sarebbe floor -> 5 // 2 = 2

        def basta_k(k):
            ore_necessarie = 0 
            for pile in piles:
                ore_necessarie += math.ceil(pile / k)   # ricorda math.ceil(dentro divisione)
            
            if ore_necessarie <= h:
                return True
            else:
                return False

        while l < r:
            mid = (l + r) // 2
            # pk non r = mid - 1? 
            # pk vogliamo mantenere mid trai candidati: potrebbe essere la v minima valida.
            if basta_k(mid):
                r = mid 
            else:
                # Escludiamo mid e tutti i valori più piccoli.
                l = mid + 1

        # pk quando il ciclo finisce, l e r sono uguali e indicano la velocità minima valida.
        return l
