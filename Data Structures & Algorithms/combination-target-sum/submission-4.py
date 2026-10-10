class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, sol, somma):
            if somma == target:
                res.append(sol.copy())
                return

            if somma > target:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, sol, somma + nums[i])
                sol.pop()

        backtrack(0, [], 0)
        return res