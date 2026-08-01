# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy node mi serve per iniziare, per avere una head fittizia
        dummy = ListNode(0)
        curr = dummy

        # non uso curr1 e curr2, uso direttamente list1 e list2
        # inoltre uso AND, quindi appena finisce una, l'altra la attacco e basta
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # aggiungo la parte rimanente
        curr.next = list1 if list1 else list2

        # restituisco la lista vera (senza il dummy!)
        return dummy.next