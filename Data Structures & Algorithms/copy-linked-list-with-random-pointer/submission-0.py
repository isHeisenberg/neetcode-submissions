"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # 1. copia nodi
        curr = head
        while curr:
            # chiave è l'oggetto curr e il valore è il nuovo nodo creato
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2. collega next e random
        curr = head
        while curr:
            # ottengo easy i nodi, dato che riferimento è il nodo curr
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            
            curr = curr.next

        # mi basta prendere il primo dalla hashamp, tanto gli altri sono collegati
        return old_to_new[head]



