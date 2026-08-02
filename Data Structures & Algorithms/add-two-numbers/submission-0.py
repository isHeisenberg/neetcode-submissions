# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        curr = dummy
        riporto = 0

        # tutto in un ciclo, inoltre anche riporto nel while, 
        # infatti potrei avere solo il riporto finale
        while curr1 or curr2 or riporto:
            # per gestire lunghezze diverse, metto if esiste e in caso pongo a 0 se è None
            val1 = curr1.val if curr1 else 0 
            val2 = curr2.val if curr2 else 0

            somma = val1 + val2 + riporto # se val1 e val2 = 0, ma riporto != 0, posso
            riporto = somma // 10 # divisione per integer -> 9 // 10 = 0, 18 // 10 = 1

            curr.next = ListNode(somma % 10)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return dummy.next

