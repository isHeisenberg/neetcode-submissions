class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node, per accesso O(1)
        
        # sentinelle: evitano controlli None sui bordi
        self.left, self.right = Node(0, 0), Node(0, 0)
        # lista vuota: LEFT <-> RIGHT
        self.left.next, self.right.prev = self.right, self.left

    '''
    Mi scrivo remove e insert che mi serviranno dentro get e put
    '''

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        # 1 <-> 2 <-> RIGHT
        # mi devo salvare il riferimento a quello dietro (2 qua)
        # infatti dovrò fare che il next di 2 è node e prev di node è 2!
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) >= self.cap:
                first = self.left.next
                del self.cache[first.key]
                self.remove(first)
            newnode = Node(key, value)
            self.cache[key] = newnode
            self.insert(newnode)














            