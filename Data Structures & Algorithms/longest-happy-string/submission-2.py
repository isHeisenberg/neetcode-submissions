class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []
        # struttura più compatta rispetta ai 3 heappush + controllo != 0
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            # non serve un counter esterno, mi basta guardare su res!
            # mi raccomando anche check su lunghezza res
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
                # per simulare il "se già trovato due volte non ci faccio nulla"
                # lo riporto dentro senza alcuna modifica al suo count
                heapq.heappush(maxHeap, (count, char))
            else:
                res.append(char)
                count += 1
                # metto dentro heap solo se ha counter != 0
                if count:
                    heapq.heappush(maxHeap, (count, char))

        return ''.join(res
        
        
        
        
        )