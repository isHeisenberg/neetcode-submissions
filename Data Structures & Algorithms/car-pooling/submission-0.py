class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        posti_liberi = capacity
        heap = []

        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                _, posti = heapq.heappop(heap)
                posti_liberi += posti
            posti_liberi -= trip[0]
            if posti_liberi < 0:
                return False
            # heapq.heappush(HEAP, x)   ricorda di mettere heap!
            heapq.heappush(heap, (trip[2], trip[0]))
        return True


'''
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
heap: ci metto (fine, persone), così chi esce prima è più in alto
'''













