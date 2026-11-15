'''
TECNICA: simulazione con sorting + min-heap

Idea:
1. Il sorting fa perdere l'indice originale, quindi lo aggiungo
   dentro ogni task: [enqueueTime, processingTime, index].
2. Ordino i task per enqueueTime, cosi' li scorro con un puntatore i
   man mano che il tempo avanza.
3. Uso un min-heap con elementi (processingTime, index):
   la CPU sceglie il task piu' corto e, a parita', quello con
   indice minore (l'ordinamento delle tuple lo fa da solo).
4. Tengo una variabile time = istante in cui la CPU si libera.
   Dopo ogni task: time += processingTime.
   
5. Se l'heap si svuota ma restano task da inserire, la CPU e' idle:
   salto time direttamente al prossimo enqueueTime.

6. Dopo aver aggiornato time, inserisco nell'heap tutti i task
   con enqueueTime <= time (sono diventati disponibili).

Il primo task (dopo il sorting) parte subito, quindi inizializzo
heap e time con lui.

Complessita': tempo O(n log n), spazio O(n).
'''


'''
FONDAMENTALE: Come faccio a partire??

Mi serve la task di partenza, cioò con minore inizio e minore tempo
faccio sorting, che a parità del primo elemento, sorta sul secondo!

PENSA SEMPRE AL SORTING SE TI SERVE UN PUNTO DI PARTENZA!
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # STRATEGIA UTILISSIMA
        # siccome faccio sorting mi perdo l'indice della task
        # quindi lo integro nell'elemento della task!
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()

        n = len(tasks)
        '''
        Nel codice iniziale start serviva per calcolare end = start + length. 
        Ma questo è corretto solo se il task parte esattamente al suo enqueue time!
        '''
        heap = [(tasks[0][1], tasks[0][2])]   # (processingTime, index)
        time = tasks[0][0]
        i = 1
        res = []

        while heap:
            proc, idx = heapq.heappop(heap)
            res.append(idx)
            time += proc

            # CPU idle: se l'heap è vuoto salto al prossimo enqueueTime
            if not heap and i < n:
                time = max(time, tasks[i][0])

            # inserisco tutti i task disponibili al tempo corrente
            while i < n and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

        return res




















        