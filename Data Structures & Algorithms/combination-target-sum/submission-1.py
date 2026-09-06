class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, sol):
            if sum(sol) == target:
                res.append(sol.copy())
                return

            if sum(sol) > target:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, sol)
                sol.pop()

        backtrack(0, [])
        return res