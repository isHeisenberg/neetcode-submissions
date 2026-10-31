# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        lunghezza = count // k
        resto = count % k

        newHead = head
        res = []

        for _ in range(k):
            curr = newHead

            if resto > 0:
                l = lunghezza + 1
                resto -= 1
            else:
                l = lunghezza

            if curr:
                for _ in range(l - 1):
                    curr = curr.next

                temp = curr.next
                curr.next = None
                res.append(newHead)
                newHead = temp
            else:
                res.append(None)

        return res






        