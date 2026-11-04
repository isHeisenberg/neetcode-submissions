'''
PARTITION EQUAL SUBSET SUM - SUBSET SUM / 0-1 KNAPSACK

Key observation:
- Voglio dividere nums in 2 gruppi con la stessa somma.
- Non devo costruire entrambi i gruppi!
- Mi basta trovare un sottoinsieme con somma = total // 2.
- Tutti gli elementi rimanenti formeranno automaticamente
  il secondo gruppo con la stessa somma.

Steps:
1. Calcolo total = sum(nums).
2. Se total è dispari -> return False (impossibile).
3. target = total // 2.
4. Uso DP per verificare se posso raggiungere target.

DP:
- dp[s] = True se posso ottenere la somma s
  usando alcuni degli elementi già visitati.
- dp[0] = True (posso ottenere 0 scegliendo niente).
- Per ogni num aggiorno le somme da target a num.
- Itero al contrario per non riutilizzare lo stesso
  elemento più volte (0/1 Knapsack).

Complexity:
- Time: O(n * target)
- Space: O(target)
'''
# CONFRONTO 0/1 KNAPSACK vs UNBOUNDED (sotto)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        # controllo anzitutto se magari si può dividere in due
        if total % 2:
            return False

        # TECNICA DEVASTANTE: definisco dp come
        # dp[i]: riesco ad arrivare all'amount i
        # vorrò alla fine target, cioè il valore di UN SOLO ARRAY
        # l'altro me ne dimentico totalmente
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        # SI TRATTA DI UN 0/1 KNAPSACK
        # Per ogni elemento decido: lo prendo oppure no?
        # Dopo aver finito un elemento lo "chiudo" e passo al prossimo,
        # cosi' non lo uso mai due volte.
        # Per cui il ciclo esterno è quello su nums
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]


'''
        for num in nums:
            for i in range(num, target + 1):
                dp[i] = dp[i] or dp[i - num]
'''
# 1 2 3 4
# target = 5
# num = 1 -> for i da(1, 6)
#   dp[1] = dp[1] o dp[0]
#   dp[2] = dp[2] o dp[1]
#   dp[3] = dp[3] o dp[2]
#   dp[4] = dp[4] o dp[3]
#   dp[5] = dp[5] o dp[4]
#   Andando avanti con indici sto riutilizzando -> non va bene

 


'''
COIN CHANGE è INVECE UN UNBOUNDED KNAPSACK
Per cui posso utilizzare una moneta tutte le volte che voglio
Dunque coins è nel CICLO INTERNO!
Se fosse stato in quello esterno avrei potuto usare 0/1 la coin!!!

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # ==========================================================
        # STEP 1: DEFINIZIONE DEL DP
        # ==========================================================
        # dp[x] = minimo numero di monete per fare esattamente x.
        #
        # INF significa "non ancora raggiungibile". Con min() un valore
        # INF non viene mai preferito a un valore reale.
        INF = float('inf')
        dp = [INF] * (amount + 1)

        # CASO BASE: per fare 0 servono 0 monete.
        dp[0] = 0

        # ==========================================================
        # STEP 2: CICLO ESTERNO SUGLI IMPORTI (IN AVANTI)
        # ==========================================================
        # Vado da 0 ad amount, cosi' quando arrivo a x tutte le celle
        # a sinistra (x - c) sono gia' FINALI, calcolate con tutte
        # le monete.
        #
        # Le monete sono infinite, quindi leggere una cella che ha gia'
        # usato la stessa moneta va bene: e' proprio il riuso che voglio.
        # Per questo qui NON serve andare al contrario.
        for x in range(amount + 1):

            # ======================================================
            # STEP 3: PROVO OGNI MONETA COME ULTIMA MONETA USATA
            # ======================================================
            for c in coins:

                # La moneta deve starci nell'importo x.
                # Se c > x, x - c sarebbe negativo.
                if x >= c:

                    # Se l'ultima moneta e' c, prima dovevo fare x - c
                    # e a quello aggiungo 1 moneta: 1 + dp[x - c].
                    # Tengo il minimo tra il valore attuale e questa
                    # nuova possibilita'.
                    dp[x] = min(dp[x], 1 + dp[x - c])

        # ==========================================================
        # STEP 4: RISULTATO
        # ==========================================================
        # Se dp[amount] e' ancora INF nessuna combinazione fa amount,
        # quindi ritorno -1. Altrimenti ritorno il minimo trovato.
        return dp[amount] if dp[amount] != INF else -1
'''


