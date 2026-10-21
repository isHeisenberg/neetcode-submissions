class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []

        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        # max-heap
        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))

        queue = deque()
        t = 0

        # while heap    non basta, infatti magari stanno in queue! con OR!
        while heap or queue:   
            if queue and queue[0][0] <= t:
                _, count, task = queue.popleft()
                heapq.heappush(heap, (-count, task))

            # infatti potrei fare pop ma il heap è vuoto
            # infatti entro nel ciclo per queue, ma heap vuoto!
            if heap: 
                # -count, task = heapq.heappop(heap) non posso fare -count quando faccio unpacking
                neg_count, task = heapq.heappop(heap)
                count = -neg_count -1

                if count > 0:
                    queue.append([t+n+1, count, task])

            t += 1

        return t

            
