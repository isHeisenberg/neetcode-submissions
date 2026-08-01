# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # slow non serve controllarlo nel while
        # fast si muove di 2 -> quindi devi verificare due passi validi
        # check su fast, pk se fast è None, fast.next scoppia
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False
        