class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        l, r = 0, 0

        for r in range(len(nums)):
            cur_sum += nums[r]  # aggiungo nuovo valore
            max_sum = max(max_sum, cur_sum) # aggiorno il massimo che ho

            if cur_sum < 0:     # se somma negativa
                l = r + 1       # butto via tutto
                cur_sum = 0     # rimetto somma a 0, la calcolo con l a prossimo ciclo

        return max_sum