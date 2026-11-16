class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # se ordine non conta, posso usare un set
        # poi itero e per ogni numero vedo se c'è quello dopo in tutto il set
        numeri = set(nums)
        massimo = 0

        for n in numeri:
            if n - 1 in numeri:
                continue

            candidate = n
            lunghezza = 1

            while candidate + 1 in numeri:
                candidate += 1
                lunghezza += 1

            massimo = max(massimo, lunghezza)

        return massimo