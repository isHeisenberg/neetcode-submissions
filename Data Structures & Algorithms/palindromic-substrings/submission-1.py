# Posso usare sia 2 Pointers che DP
# 2 Pointers ottimale: O(n^2) in tempo e solo O(1) in spazio
# DP non è ottimale, ma qui si può usare perchè soddisfo 2 condizioni:
#   1. Posso suddividere in sottoproblemi
#   2. Questi sono collegati tra loro
class Solution:
    def countSubstrings(self, s: str) -> int:
        # matrice n x n di bool
        # dp[l][r]: s[l:r+1] è palindromo -> complessità O(n^2)
        n = len(s)
        dp = [ [False] * n for _ in range(n) ]

        res = 0

        # IMPORTANTE: metti n-1 se metti len come inizio, in quanto è inclusivo
        # SOLO IL TERMINE è ESCLUSO! Infatti -1 raggiunge 0 e si ferma 
        for l in range(n-1, -1, -1):    # l va a sinistra
            for r in range(l, n):       # r va a destra 
                if s[r] == s[l] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    res += 1

        return res


# se l==r allora guardo, il caso prima più stretto (l+1, r-1) l'avevo già fatto?
# se sì, top non bisogno di controllare in mezzo
# caso r-l <= 2 copre i casi base, dove non ha senso controllare dp[l+1][r-1]:
# r - l == 0: (es. "a"), sempre palindromo da solo.
# r - l == 1: (es. "aa"), palindromo se sono uguali, non serve controllare l'interno
# r - l == 2: (es. "aba"), interno è un solo carattere, che è sempre palindromo da solo


