class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = {}
        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1


        # Se una lettera occupa più della metà è impossibile riorganizzare 
        if max(counter.values()) > (len(s) + 1) // 2:
            return ""
        
        heap = []

        for k,v in counter.items():
            heapq.heappush(heap, (-v, k))

        res = []
        temp = None
        while heap:
            count, val = heapq.heappop(heap)
            res.append(val)
            count += 1

            if temp != None:                
                heapq.heappush(heap, temp)

            if count != 0:  # non rimetto subito dentro al heap!
                temp = (count, val)
            else:           # sennò resta un valore vecchio
                temp = None

        return "".join(res) 




