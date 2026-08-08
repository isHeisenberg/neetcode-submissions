class KthLargest:
    # nel minHeap ci sono quelli più piccoli
    # tuttavia ogni volta che faccio pop, tolgo il più piccolo
    # per cui facendo pop fino a quando ne rimangono k
    # è un modo smart per tenere quindi i 5 più grandi
    # in quanto i più piccoli li ho tolti tutti
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # da array normale a heap
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # ne tengo k

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

