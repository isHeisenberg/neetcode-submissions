class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        sol = []
        def backtrack(i, somma):    
            if somma == target:
                res.append(sol.copy())
                return
            elif somma > target:
                return
            elif i >= len(nums):
                return

            # metto solo i (non i+1) così posso riutilizzare l'elemento
            sol.append(nums[i])
            backtrack(i, somma + nums[i])
    
            sol.pop()
            backtrack(i+1, somma)

        backtrack(0, 0)
        return res