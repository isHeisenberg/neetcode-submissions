# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        dummy = ListNode(0, head)
        curr = dummy
        while counter < n and curr != None:
            counter += 1
            curr = curr.next

        if counter < n:
            return dummy.next

        prev = dummy
        while curr and curr.next:
            curr = curr.next
            prev = prev.next

        # ora mi trovo prima del nododa togliere
        prev.next = prev.next.next
        return dummy.next


