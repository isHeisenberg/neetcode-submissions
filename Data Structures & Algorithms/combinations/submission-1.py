class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol.copy())
                return
            
            if i == n+1:
                return 

            sol.append(i)
            backtrack(i+1)
            sol.pop()
            backtrack(i+1)


        backtrack(1)
        return res