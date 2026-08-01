class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:  # stops slow at correct midpoint
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next  # mi aggancio a inizio seconda metà
        slow.next = None  # cut the list here before reversing PER EVITARE LOOP INFINITO

        # inverto la seconda metà
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # slow.next = prev <- removed, this would undo the cut
        second = prev

        first = head
        while second:
            firstNext = first.next
            first.next = second
            secondNext = second.next
            second.next = firstNext
            first = firstNext
            second = secondNext

