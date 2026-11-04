'''
Perché il tuo approccio non funziona

Hai dp[i] = modi per fare la somma i, e per ogni num provi sia +num sia -num. Due problemi:

Le somme intermedie escono dall'intervallo [0, target]. Con nums = [1, 1, 1, 1, 1] e target = 3, una soluzione è +1+1+1+1-1: passi per somme come 4, che è maggiore di 3. Se limiti l'array a target, tagli via percorsi validi. Le somme intermedie possono andare da -total a +total.
Il ritroso con in-place non regge due direzioni. Con i + num leggi un indice maggiore (già aggiornato in questa passata), con i - num uno minore (non ancora aggiornato). Mescoli vecchio e nuovo stato nella stessa passata, quindi i conteggi sono sbagliati.
'''
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # considero il target positivo (è la stessa cosa)
#         # btw tutti i nums sono positivi, no check
#         target = abs(target)

#         # dp[i]: in quanti modi riesco a fare i
#         dp = [0] * (target + 1)
#         dp[0] = 1

#         # 0/1 KNAPSACK
#         # Quindi vado da fine a inizio
#         for num in nums:
#             for i in range(target, num - 1, -1):
#                 # da checkare
#                 if i + num in range(target+1):
#                     dp[i] = dp[i] + dp[i + num]
#                 if i - num in range(target+1):
#                     dp[i] = dp[i] + dp[i - num]

#         return dp[target]









'''
TARGET SUM - SUBSET SUM / 0-1 KNAPSACK (conteggio)

Problema:
- Per ogni num scelgo il segno + oppure -.
- Voglio contare in quanti modi la somma finale vale target.

Key observation (la riduzione a P):
- Chiamo P la somma dei numeri col segno +.
- Chiamo N la somma dei numeri col segno - (come numero positivo).
- Valgono due fatti:
    P + N = total     (ogni numero sta nel gruppo + o nel gruppo -)
    P - N = target    (condizione del problema)
- Sommando le due equazioni: 2P = total + target
    P = (total + target) // 2

- Non devo decidere + o - per ogni numero.
  Mi basta scegliere QUALI numeri vanno nel gruppo + (somma P).
  Quelli rimasti vanno automaticamente nel gruppo -.


- Il problema diventa: in quanti modi scelgo un sottoinsieme
  con somma P? Ogni elemento ha UNA sola scelta (prendo / non prendo),
  quindi è un 0/1 knapsack!



Perché NON il DP diretto su +/-:
- Le somme intermedie vanno da -total a +total, non restano in [0, target].
- Con un solo array in place non si possono gestire +num e -num insieme:
  si mescolerebbe stato vecchio e stato nuovo nella stessa passata.

Casi impossibili (return 0):
- abs(target) > total: P uscirebbe dall'intervallo valido
  (con target molto negativo P < 0 e dp avrebbe dimensione sbagliata).
- (total + target) dispari: P verrebbe arrotondato per difetto
  e il DP conterebbe un problema diverso da quello originale.

DP:
- dp[s] = in quanti modi scelgo un sottoinsieme di nums con somma s.
- dp[0] = 1 (un solo modo per fare 0: non scegliere niente).
- Per ogni num aggiorno da P a num, in ritroso:
  dp[s] += dp[s - num]
- Ritroso = ogni elemento usato al massimo una volta (0/1).
  In avanti sarebbe unbounded (elemento riusabile).

Esempio nums = [2, 2, 2], target = 2:
- total = 6, P = (6 + 2) // 2 = 4
- dp parte da [1, 0, 0, 0, 0]
- dopo il primo 2:  [1, 0, 1, 0, 0]
- dopo il secondo 2: [1, 0, 2, 0, 1]
- dopo il terzo 2:  [1, 0, 3, 0, 3]
- risposta dp[4] = 3

Zeri:
- Con num = 0 il ciclo include s = 0 e dp[0] += dp[0] raddoppia il conteggio.
  È corretto: uno zero può essere +0 oppure -0 (due modi distinti).
  Nessun caso speciale.

Complexity:
- Time: O(n * P)
- Space: O(P)
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0

        P = (total + target) // 2

        dp = [0] * (P + 1)
        dp[0] = 1

        # 0/1 KNAPSACK: ritroso
        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]

        # Codice 0/1 è sempre lo stesso, questo di partition sum
        # for num in nums:
        #     for s in range(target, num - 1, -1):
        #         dp[s] = dp[s] or dp[s - num]  era booleano

        return dp[P]



