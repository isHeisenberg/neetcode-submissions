'''
2D Dynamic Programming (Bottom-Up / Tabulation).

dp[i][j] = LCS massima tra text1[i:] e text2[j:].

Si parte dal fondo e si procede verso l'inizio.

- Caratteri uguali: 1 + diagonale (dp[i+1][j+1]).
- Caratteri diversi: max tra saltare un carattere di text1 o text2.

La riga e colonna extra inizializzate a 0 rappresentano i casi base (stringa vuota).

Time: O(m * n)
Space: O(m * n)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]