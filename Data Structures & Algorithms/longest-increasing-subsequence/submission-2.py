# LIS[i] = lunghezza della più lunga sottosequenza crescente
# che INIZIA dalla posizione i

'''
Puoi definire la LIS anche al contrario, cioè come la più lunga sottosequenza crescente che FINISCE in i.

Il tuo ragionamento è naturale: scorriamo da sinistra a destra, quindi verrebbe da definire dp[i] come la LIS che inizia in i.

Il problema è che, se sei in i, per sapere quanto è lunga la sequenza che inizia lì, devi conoscere cosa succede dopo i. Ma non l'hai ancora visitato!


quindi il come definisco dp deve dipendere strettamente dal fatto di "quali dati ho già e posso riutilizzare", per cui io avrei detto tipo inizialmente più lunga che parte da i, per sapere bohhh non saprei manco che valori prendere. che finisce in i, allora ciclo su quelli prima


Hai centrato il punto.

La definizione del DP deve essere legata a quali informazioni hai già calcolato e puoi riutilizzare.

Nel tuo caso, ragioniamo così:
1. Scorro da sinistra a destra.
2. Arrivo in posizione i.
3. Conosco già tutti gli elementi precedenti e ho calcolato i rispettivi DP.
4. Posso quindi chiedermi: qual è la sequenza crescente più lunga che termina proprio qui?
5. Per rispondere, guardo gli elementi precedenti più piccoli e riutilizzo i loro DP.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

# O(n^2) time
# O(n) memory

'''

# TOP-DOWN
def dfs(i):
    if i == len(s): # base
        return True
    for word in wordDict:
        if s.startswith(word, i):
            if dfs(i + len(word)): # chiama indici maggiori
                return True
    return False
'''