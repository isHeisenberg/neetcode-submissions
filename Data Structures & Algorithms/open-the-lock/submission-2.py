'''
NOTE IMPORTANTI:

- Il modulo sui numeri negativi
-1 % 10 => -1*10 + x = -1 => 9 FORMULA
-1 % 10 = 9, perché (-1 = (-1)*10 + 9)   

- for direction in [1, -1]:
utile per considerare sia negativo che positivo comodamente

- STRINGHE SONO IMMUTABILI IN PYTHON
creo una nuova stringa, infatti stringhe immutabili
non posso modificarla, ma necessario crearne un'altra
esempio: newnumber = (number[:i] + new_num + number[i+1:])

- ricorda di mettere il caso iniziale in tutte le strutture dati
quindi sia queue che visited!

- NOTA BENE: stringhe lunghe 4, slicing stringhe è O(4) -> lo uso
La versione con interi potrebbe essere leggermente più veloce:
- Gli interi sono generalmente più economici da confrontare e memorizzare.
- Le stringhe richiedono slicing e concatenazione per generare i vicini.
Se lunghezza indefinita numeri, allora meglio passare a numeri int

'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        if "0000" in dead:
            return -1

        visited = set("0000")           # ricorda di mettere inizio qua!
        queue = deque([("0000", 0)])    # non deque(("0000", 0))


        # parto da stringa e ho ciclo for in cui aumento di 1 o -1 per ogni cifra
        # se è un deadend torno indietro e faccio -1
        def bfs():
            while queue:
                number, counter = queue.popleft()

                if number == target:
                    return counter

                for i in range(4):
                    num = int(number[i])

                    for direction in [1, -1]:
                        # 9+1 = 10 % 10 = 0
                        # 0-1 = -1 % 10 = 9
                        # 8 % 10 = 8, perché (8 = 0*10 + 8)
                        # -1 % 10 = 9, perché (-1 = (-1)*10 + 9)   
                        new_num = str((num + direction) % 10)

                        # creo una nuova stringa, infatti stringhe immutabili
                        # non posso modificarla, ma necessario crearne un'altra
                        newnumber = (
                            number[:i] + new_num + number[i+1:]
                        )

                        if newnumber not in visited and newnumber not in dead:
                            visited.add(newnumber)
                            queue.append((newnumber, counter + 1))

            return -1
        
        return bfs()
