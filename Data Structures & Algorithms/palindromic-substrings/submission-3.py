class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[x][y] = True if substring s[x:y+1] è un palindromo
        dp = [ [False] * n for _ in range(n) ]
        counter = n
        for i in range(n):
            dp[i][i] = True

        # Considero tutte le lunghezze per delle substring
        for length in range(2, n+1):
            # Data la lunghezza so fino a dove posso arrivare per non sforare
            for i in range(n - length + 1):
                j = i + length - 1  # estremo destro lo trovo grazie a length

                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1]:
                        counter += 1
                        dp[i][j] = True

        return counter