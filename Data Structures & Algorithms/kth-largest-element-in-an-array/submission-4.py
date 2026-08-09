class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topK = []

        # prendo i k elementi più grandi
        for num in nums:
            heapq.heappush(topK, num)
            if len(topK) > k:
                heapq.heappop(topK)
        
        # il k-esimo più grande (cioè il minore nel heap) è sulla root!
        return topK[0] 


        