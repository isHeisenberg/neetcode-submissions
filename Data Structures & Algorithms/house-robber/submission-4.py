class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0       # nessuna casa vista ancora

        # rob1 = il massimo bottino fino a due case fa
        # rob2 = il massimo bottino fino alla casa precedente
        for num in nums:
            temp = max(num + rob1, rob2)   # rubo questa o tengo il max precedente?
            rob1 = rob2         # "due case fa" diventa "una casa fa"
            rob2 = temp         # il nuovo massimo diventa il valore corrente

        return rob2             # risultato finale


