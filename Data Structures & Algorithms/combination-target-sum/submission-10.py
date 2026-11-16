class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i, somma):
            if somma == target:
                res.append(sol.copy())
                return
            if i >= len(nums) or somma > target:
                return 

            sol.append(nums[i])
            backtrack(i, somma+nums[i])
            sol.pop()
            backtrack(i+1, somma)
            
            return

        backtrack(0, 0)
        return res