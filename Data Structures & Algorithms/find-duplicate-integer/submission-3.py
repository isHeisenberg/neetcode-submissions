class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #len = n+1
        # ci sono dei numeri diversi, solo uno si ripete anche più volte
        # tutti tra [1, n]
        # posso usare set O(n) in tempo e spazio

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)