class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sol = []

        def backtrack(start, somma):
            if somma == target:
                res.append(sol.copy())
                return

            if somma > target or start == len(candidates):
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                sol.append(candidates[i])
                backtrack(i + 1, somma + candidates[i])
                sol.pop()

        backtrack(0, 0)
        return res