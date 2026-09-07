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
            for j in range(i + 1, len(nums)):
                if nums[j] != nums[i]:
                    break
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return res