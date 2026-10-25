class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #len = n+1
        # ci sono dei numeri diversi, solo uno si ripete anche più volte
        # tutti tra [1, n]
        # posso usare set O(n) in tempo e spazio
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        # Fase 1: trova un punto dentro il ciclo
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]          # 1 passo
            fast = nums[nums[fast]]    # 2 passi
            if slow == fast:
                break

        # Fase 2: trova l'ingresso del ciclo (il duplicato)
        # Si incontrano sicuro perché le distanze sono costruite per coincidere esattamente. 
        # E il duplicato è l’ingresso del ciclo!
        slow = nums[0]  # riparto dall'inizio
        while slow != fast:
            slow = nums[slow]          # 1 passo
            fast = nums[fast]          # 1 passo

        return slow



