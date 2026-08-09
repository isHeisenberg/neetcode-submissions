class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            distance = point[0]**2 + point[1]**2 # non serve sqrt
            elem = [-distance, point[0], point[1]]
            heapq.heappush(res, elem)

            if len(res) > k:
                heapq.heappop(res)

        # risultato = []
        # for point in res:
        #     risultato.append([point[1], point[2]])
        
        # return risultato

        return [[point[1], point[2]] for point in res] 


