class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        somma = 0
        minlen = float('inf')

        for r in range(len(nums)):
            somma += nums[r]

            while somma >= target:
                minlen = min(minlen, r - l + 1)
                somma -= nums[l]
                l += 1

        return 0 if minlen == float('inf') else minlen