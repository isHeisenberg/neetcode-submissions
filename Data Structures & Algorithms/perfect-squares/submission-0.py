'''
Per confutare un approccio greedy, cerca un controesempio.

Prova un caso in cui la scelta localmente migliore
impedisce di ottenere la soluzione globalmente ottimale.

Esempio: numSquares, n = 12

Greedy: 9 + 1 + 1 + 1 = 4 quadrati
Ottimo: 4 + 4 + 4 = 3 quadrati

Direi basta partire mettendo 3 "4" e vedere se faccio meglio greedy
'''

# UNBOUNDED KNAPSACK
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while True:
            sq = i**2
            if sq > n:
                break
            squares.append(sq)
            i += 1 

        # dp[i]: minimo numero di quadrati per raggiungere i
        # ATTENTO: va inizializzato a infinito per trovare minimo!
        dp = [float('inf')] * (n+1)  
        dp[0] = 0

        for i in range(1, n+1):
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i], 1 + dp[i-square])
        
        return dp[-1]














'''
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while True:
            sq = i**2
            if sq > n:
                break
            squares.append(sq)
            i += 1 

        i = len(squares) - 1
        counter = 0
        while i >= 0:
            if n - squares[i] > 0:
                n -= squares[i]
                counter += 1
            else:
                i -= 1
        
        return counter
'''