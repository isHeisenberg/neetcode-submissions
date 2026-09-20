# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # Controllo che ci siano k nodi
            # Pk ribalto solo gruppi da k elementi
            node = curr

            for _ in range(k):
                if node is None:
                    return dummy.next
                node = node.next

            # Ribalta il gruppo
            for _ in range(k - 1):
                temp = curr.next

                curr.next = temp.next

                temp.next = prev.next
                prev.next = temp

            # curr è ora l'ultimo nodo del gruppo
            prev = curr
            curr = curr.next

        return dummy.next






