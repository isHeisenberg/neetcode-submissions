class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []

        def backtrack(i):
            if i == len(nums):
                res.append(sol.copy())
                return

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # se il prossimo è uguale, salto il duplicato
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return res