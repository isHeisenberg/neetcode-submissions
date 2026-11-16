class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        max_len = 1
        n = len(s)
        dp = [ [False] * n for _ in range(n) ]
        # quelli con un solo elemento sono palindromi
        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if dp[i+1][j-1] or length == 2:
                        dp[i][j] = True
                        idx = i
                        max_len = length

        return s[idx:max_len+idx]
