'''
Sliding Window: mantengo una finestra turbolenta [l, r].
- prev memorizza l'ultimo confronto (< oppure >).
- Se il confronto attuale è opposto a prev, estendo la finestra.
- Se il confronto è uguale a prev, riparto da r-1.
- Se due elementi sono uguali, avanzo e riparto da r.
- Aggiorno res ad ogni estensione valida.

Time: O(n) | Space: O(1)
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            # il != ">" mi prende sia "" che "<", top!
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res












'''
Backtracking: provo ogni possibile punto di partenza del subarray.
- i: ultimo indice raggiunto.
- length: lunghezza del subarray corrente.
- prev: ultimo confronto (1 = crescente, -1 = decrescente, 0 = nessuno).

Se prev == 0, posso iniziare sia crescendo che decrescendo.
Se prev == 1, il prossimo confronto deve essere decrescente.
Se prev == -1, il prossimo confronto deve essere crescente.

Se il confronto è valido, avanzo ricorsivamente aggiornando
indice, lunghezza e direzione.
Se non è valido, termino il percorso.

Ad ogni chiamata aggiorno la lunghezza massima trovata.
Il for finale prova tutti i possibili indici iniziali.

Time: O(n²) | Space: O(n) per lo stack ricorsivo.

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        self.res = 1

        def backtrack(i, length, prev):
            self.res = max(self.res, length)

            if i >= len(arr) - 1:
                return

            if prev == 0:
                if arr[i] < arr[i + 1]:
                    backtrack(i + 1, length + 1, 1)
                elif arr[i] > arr[i + 1]:
                    backtrack(i + 1, length + 1, -1)

            elif prev == 1:  # Ultimo confronto crescente
                if arr[i] > arr[i + 1]:
                    backtrack(i + 1, length + 1, -1)

            elif prev == -1:  # Ultimo confronto decrescente
                if arr[i] < arr[i + 1]:
                    backtrack(i + 1, length + 1, 1)

        for i in range(len(arr)):
            backtrack(i, 1, 0)

        return self.res
'''


        