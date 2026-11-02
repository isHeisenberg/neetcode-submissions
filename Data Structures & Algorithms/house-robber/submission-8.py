class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # dp[i]: massimo rubabile nelle case da 0 a i
        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            a, b = b, max(nums[i] + a, b)

        return b