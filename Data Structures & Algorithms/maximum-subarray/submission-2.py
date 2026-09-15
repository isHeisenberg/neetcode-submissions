class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]  # aggiungo nuovo valore
            max_sum = max(max_sum, cur_sum) # aggiorno il massimo che ho

            if cur_sum < 0:     # se somma negativa
                cur_sum = 0     # butto via tutto

        return max_sum



