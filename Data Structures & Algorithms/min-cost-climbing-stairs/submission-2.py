'''
Il trucco per ricordarlo

Ogni volta che fai dp, chiediti tre cose:

Cosa rappresenta lo stato? (qui: costo per arrivare a i)
Da dove posso arrivarci? (da i-1 o da i-2)
Qual è il caso base? (dp[0] = dp[1] = 0)
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i]: costo minimo per raggiungere il gradino i
        dp = [0] * (n + 1)

        '''
        Per arrivare al gradino i hai solo due modi:

        Arrivi da i-1 e fai 1 passo: paghi cost[i-1] per partire da lì.
        Arrivi da i-2 e fai 2 passi: paghi cost[i-2].

        Quindi: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        “costo per arrivare al gradino da cui parto + costo per ripartire da lì”.
        '''
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]




'''
VERSIONE CON MENO MEMORIA:

def minCostClimbingStairs(self, cost):
    n = len(cost)
    a, b = 0, 0  # dp[i-2], dp[i-1]
    for i in range(2, n + 1):
        a, b = b, min(b + cost[i - 1], a + cost[i - 2])
    return b
'''






    