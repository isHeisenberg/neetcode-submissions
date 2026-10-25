"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# posso creare la lista normale con random = None in tutti e poi ciclo in cui assegno i random?
# per assegnare random devi sapere quale nodo nuovo corrisponde al random del vecchio nodo, e scorrere la lista per trovarlo costerebbe O(n) per ogni nodo (O(n²) totale)

'''
DUE PASSATE:

Prima passata: crei una copia di ogni nodo (solo val) 
e la salvi in un dizionario con chiave il nodo originale.
Seconda passata: per ogni nodo originale, 
colleghi next e random della copia usando il dizionario.
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copia = {}

        # 1) creo tutte le copie
        cur = head
        while cur:
            copia[cur] = Node(cur.val)
            cur = cur.next

        # 2) collego next e random
        cur = head
        while cur:
            copia[cur].next = copia.get(cur.next)
            copia[cur].random = copia.get(cur.random)
            cur = cur.next

        return copia[head]

