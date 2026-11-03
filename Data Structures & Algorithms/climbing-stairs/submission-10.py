class Solution:
    def climbStairs(self, n: int) -> int:
        #dp = [0] * (n+1)
        #dp[0] = 1
        #dp[1] = 1
        a = 1
        b = 1

        for i in range(2, n+1):
            b, a  = b + a, b
            #dp[i] = dp[i-1] + dp[i-2]
        
        return b