'''
LFU Cache: rimuove la chiave meno frequentemente utilizzata.
- nodeMap: mappa key -> node per accesso O(1).
- listMap: mappa frequenza -> lista doppiamente concatenata.
- Ogni lista contiene nodi con la stessa frequenza, ordinati per recenza.
- get / update: rimuovi il nodo dalla vecchia lista, incrementa freq e inseriscilo nella nuova.
- put: se la cache è piena, elimina il nodo meno recente dalla lista con frequenza minima.
- lfuCnt: mantiene la frequenza minima globale per evitare scansioni.

Pattern riutilizzabili:
- HashMap + Doubly Linked List per accesso e rimozione O(1).
- Più linked list organizzate tramite una HashMap.
- Dummy head/tail per semplificare inserimenti e rimozioni.
- Variabile globale per mantenere il minimo senza cercarlo ogni volta.
'''
class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.nodeMap = {} # Map key -> node
        # Map frequency -> linkedlist of nodes
        self.listMap = defaultdict(LinkedList)

    def counter(self, node):
        cnt = node.freq
        self.listMap[cnt].pop(node)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

        node.freq += 1
        self.listMap[node.freq].pushRight(node)


    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        if len(self.nodeMap) == self.cap:
            node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key)

        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.lfuCnt = 1










