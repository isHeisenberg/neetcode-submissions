class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        heap = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            n_freq, num = heapq.heappop(heap)
            res.append(num)

        return res
        