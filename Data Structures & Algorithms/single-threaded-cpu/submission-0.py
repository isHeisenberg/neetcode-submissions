'''
tasks[i] = [enqueueTimei, processingTimei]
disponibile al tempo task[i][0] e dura task[i][1]

1 processo alla volta

1. if idle AND no tasks available -> remain idle
2. if idle AND tasks available -> 
    a. choose shortest (min(task[i][1]))
    b. otherwise, the first (min(task[i][0]))

la fa da inizio a fine da sola
nuova inizia a task[i][0] + task[i][1] (subito dopo =)



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




















        