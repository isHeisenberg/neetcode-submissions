class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            # se esiste di num me lo dà, altrimenti dà 0. E ci devo sommare 1
            counter[num] = counter.get(num, 0) + 1

        res = []
        
        threshold = len(nums) // 3
        for key, value in counter.items():
            if value > threshold:
                res.append(key)

        return res
