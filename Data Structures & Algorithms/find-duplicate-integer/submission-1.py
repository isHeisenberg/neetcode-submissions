# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
        # seen = {}
        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        #     if (seen[num]) > 1:
        #         return num

# soluzione usando linked list logic: uso valori come indici per i next
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # fase 1: trova un punto nel ciclo
        while True:
            slow = nums[slow]         # 1 passo
            fast = nums[nums[fast]]   # 2 passi
            if slow == fast:
                break                 # si incontrano nel ciclo

        # fase 2: trova l'inizio del ciclo (duplicato)
        slow = nums[0]                # riparti dall'inizio
        while slow != fast:
            slow = nums[slow]        # 1 passo
            fast = nums[fast]        # 1 passo

        return slow                   # duplicato
        