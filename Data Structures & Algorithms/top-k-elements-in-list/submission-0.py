class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        # 1: 4
        # 2: 3
        
        # ordina per frequenza (decrescente)
        sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
