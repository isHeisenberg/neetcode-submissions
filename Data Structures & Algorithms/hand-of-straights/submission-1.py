'''
ERRORI FATTI:
1. IndexError: heap vuoto dopo i pop -> while heap and ..., poi if not heap: break
2. KeyError: val può non esistere -> frequencies.get(val, 0)

PER CUI RICORDATI SEMPRE I CHECK SU DICT E HEAP
SPECIALMENTE SE STAI FACENDO DEI heapq.heapPOP
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequencies = {}
        for num in hand:
            frequencies[num] = frequencies.get(num, 0) + 1

        heap = list(frequencies.keys())
        heapq.heapify(heap)

        while heap:
            # siccome è un while in cui faccio pop
            # mi devo tenere anche un check su heap 
            while heap and frequencies[heap[0]] == 0:
                heapq.heappop(heap) 
            if not heap:
                break

            for i in range(groupSize):
                val = heap[0] + i
                #if frequencies[val] != 0:  # se non c'è val esplode
                if frequencies.get(val, 0) > 0:
                    frequencies[val] -= 1
                else:
                    return False
        
        return True
            





'''
from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for card in hand:
            # 1. risali fino all'inizio della sequenza
            start = card
            while count[start - 1] > 0:
                start -= 1

            # 2. da start fino a card, crea i gruppi che iniziano in 'start'
            while start <= card:
                while count[start] > 0:
                    for i in range(start, start + groupSize):
                        if count[i] == 0:
                            return False
                        count[i] -= 1
                start += 1

        return True
'''
