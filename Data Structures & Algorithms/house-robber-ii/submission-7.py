class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def r(arr):
            # dp[x] = massimo rubato nei primi i
            n = len(arr)
            dp = [0] * (n+1) # ricorda la parentesi
            dp[1] = arr[0]

            for i in range(2, n+1): # coerenza con dimensione dp
                dp[i] = max(dp[i-1], arr[i-1] + dp[i-2])

            return dp[n]
        
        # ricorda che il end non viene considerato, quindi
        # devo mettere -1, per cui -1 non viene preso ed è fino al penultimo
        # avevo messo -2, che mi toglieva pure il penultimo!
        #return max(nums[0], r(nums[0:-2]), r(nums[1:-1]))
        return max(nums[0], r(nums[:-1]), r(nums[1:]))