class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        # -4 -3 -2 -1
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # two pointers
                l, r = j+1, n-1
                while l < r:
                    somma = nums[i] + nums[j] + nums[l] + nums[r]
                    if somma == target:
                        lista = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(lista)
                        vecchio_l = l
                        # itero finchè num diversi da quelli che ho
                        while nums[l] == nums[vecchio_l] and l < n-1:
                            l += 1                         
                    if somma < target:
                        l += 1
                    else:
                        r -= 1

        return res
