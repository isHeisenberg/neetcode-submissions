class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(0, len(nums)):
        #     prod = 1
        #     for j in range(0, len(nums)):
        #         if (i != j):
        #             prod *= nums[j]
            
        #     output.append(prod)
        
        # return output

        n = len(nums)
        output = [1] * n

        # prodotti da sinistra
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # prodotti da destra
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
