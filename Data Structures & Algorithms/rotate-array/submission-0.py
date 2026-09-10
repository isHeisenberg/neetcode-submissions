# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= n            

#         def reverse(arr):   # devo passare indici e modificare direttamente qua nums
#             l, r = 0, len(arr) - 1
#             while l <= r:
#                 arr[l], arr[r] = arr[r], arr[l]
#                 l += 1
#                 r -= 1
        
#         l, r = 0, len(nums) - 1
#         for _ in range(k):
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
        
#         # NON VA BENE
#         # Lo slice crea un nuovo array, non sto lavorando e modificando nums!
#         reverse(nums[:len(nums) - k])   
#         reverse(len(nums) - k + 1:)
#         reverse(k, n-1)



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k %= n  # comodo, tanto ci rigira

        def reverse(l, r):  # li dò gli indici direttamente
            while l < r:
                # uso diretto nums, tanto ne ho accesso, dato che sub-function
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1
                r -= 1

        reverse(0, n - 1)   # ruoto tra loro le due metà
        reverse(0, k - 1)   # ruoto la prima da sola
        reverse(k, n - 1)   # ruota la seconda da sola



