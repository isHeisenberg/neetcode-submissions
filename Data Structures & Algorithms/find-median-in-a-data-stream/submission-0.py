class MedianFinder:
    def __init__(self):
        # small: max-heap (valori negati), metà inferiore
        # large: min-heap, metà superiore
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 1. Scelta dell'heap: se num sta nella metà alta va in large,
        #    in tutti gli altri casi (compreso large vuoto) va in small
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # 2. Ribilanciamento: le dimensioni non devono differire di più di 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)  
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)   
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Numero dispari di elementi: la mediana è la cima dell'heap più grande
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # Numero pari: media 
        return (-self.small[0] + self.large[0]) / 2.0


        