class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        sol = []

        def backtrack(i, somma):
            if somma == target:
                res.append(sol.copy())
                return
            elif somma > target or i >= len(candidates):
                return

            sol.append(candidates[i])
            backtrack(i+1, somma + candidates[i])

            val = sol.pop()
            while i < len(candidates) and candidates[i] == val:
                i += 1
            backtrack(i, somma)

        backtrack(0, 0)
        return res