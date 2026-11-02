'''
Il pattern: “contare i modi” con DP sul prefisso/suffisso

Guarda una sola scelta alla volta. Fissa la posizione i e chiediti: come posso consumare l’inizio del pezzo che resta? Qui: 1 cifra o 2 cifre.

Il resto è lo stesso problema, più piccolo. Dopo la scelta, ti rimane un suffisso. Definisci dp[i] = risposta per s[i:].

Scelte alternative si sommano. dp[i] = (se scelta A valida) dp[i+1] + (se scelta B valida) dp[i+2]. Ogni scelta ha la sua condizione di validità.

Caso base = “niente da fare” vale 1. La stringa vuota ha 1 modo, così la somma funziona.

Riempi dalla fine verso l’inizio, perché dp[i] dipende da indici più grandi.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = numero di modi per decodificare il suffisso s[i:]
        dp = [0] * (n + 1)
        dp[n] = 1

        # Riempi dalla fine verso l’inizio, 
        # perché dp[i] dipende da indici più grandi.
        for i in range(n - 1, -1, -1):
            # se suffisso s[i:] inizia con 0, allora 0 modi in essa
            if s[i] == "0":
                dp[i] = 0
            else:
                # Se s[i] non è "0", la cifra da sola è una lettera ok
                # e usarla da sola non cambia il numero di modi del resto.
                dp[i] = dp[i + 1]

            if i + 1 < n and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]
