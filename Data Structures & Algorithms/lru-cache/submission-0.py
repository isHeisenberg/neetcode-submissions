class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None  # bidirez

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node, per accesso O(1)

        # sentinelle: evitano controlli None sui bordi
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        # lista vuota: LEFT <-> RIGHT

    def remove(self, node):
        # stacca il nodo dalla lista
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # inserisce il nodo subito a sinistra di RIGHT (= posizione più recente)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # sposta in posizione più recente
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1  # non trovato

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # rimuovi versione vecchia
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])  # inserisci come più recente

        if len(self.cache) > self.cap:
            # LEFT.next è il nodo meno recente: eliminalo
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]  # sincronizza la mappa

            