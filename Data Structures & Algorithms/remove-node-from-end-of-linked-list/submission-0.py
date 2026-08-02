# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 0
        while count < n and fast:
            fast = fast.next
            count += 1 
        
        dummy = ListNode(0, head)
        prev = dummy
        slow = head

        while fast:
            fast = fast.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next

        return dummy.next










