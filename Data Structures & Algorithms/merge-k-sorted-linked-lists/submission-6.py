class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # se uso una funzione che richiamo dentro, devo definirla prima di usarla
        # altrimenti fuori, sotto Solution come sempre classico
        def mergeLists(l1, l2):
            dummy = ListNode(0, None)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            return dummy.next 

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                lista1 = lists[i]
                lista2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergeLists(lista1, lista2))
            lists = merged

        return lists[0]

