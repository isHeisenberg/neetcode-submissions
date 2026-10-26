class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            heap.append((dist, point))
            
        heapq.heapify(heap) # O(n), mentre i continui push -> n * logn

        res = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)

        return res