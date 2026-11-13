# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(num1, num2):
            n = min(num1, num2)
            for i in range(n, 0, -1):
                if num1 % i == 0 and num2 % i == 0:
                    return i 

        curr = head
        while curr.next:
            prox = curr.next
            mid = ListNode(gcd(curr.val, prox.val), curr.next)
            curr.next = mid
            curr = prox

        return head