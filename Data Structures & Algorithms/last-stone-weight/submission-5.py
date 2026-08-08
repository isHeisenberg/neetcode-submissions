class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length = len(stones)
        minHeap = []
        for stone in stones:
            minHeap.append(-stone)
    
        # errore, non restituisce, ma modifica in-place
        # minHeap = heapq.heapify(negative_stones)
        heapq.heapify(minHeap)

        while minHeap and len(minHeap) > 1:
            # heappop è un metodo di heapq e non della lista!!!
            # stone1 = minHeap.heappop()
            stone1 = heapq.heappop(minHeap)
            stone2 = heapq.heappop(minHeap)

            delta = stone1 - stone2
            if delta != 0:
                heapq.heappush(minHeap, delta)
        
        # ricorda di ritornare col segno a positivo
        return -minHeap[0] if minHeap else 0 


