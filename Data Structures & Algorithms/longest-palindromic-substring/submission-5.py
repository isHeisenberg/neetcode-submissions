class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[x][y]: True se s[x:y+1] è palindromo
        n = len(s)
        dp = [ [False] * n for _ in range(n) ]
        # se in array c'è un solo elemento, allora True, è palindromo
        for i in range(n):
            dp[i][i] = True
        
        max_len = 1
        start = 0

        for length in range(2, n + 1): # lunghezza deve arrivare a n
            for i in range(n - length + 1): # +1 così 
                j = i + length - 1  # estremo destro

                if s[i] == s[j]:
                    # lunghezza 2: nessun interno da controllare
                    # lunghezza > 2: l'interno [j+1 a j-1] deve essere palindromo, infatti dp[x][y] = s[x:y+1] 
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            max_len = length
                            start = i

        # smart usare il max_len e non doppio indice
        return s[start:start + max_len] 

