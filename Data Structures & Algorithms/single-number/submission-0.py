class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        # XOR: se bit uguali -> 0
        for num in nums:
            res = num ^ res     # XOR = ^
        return res