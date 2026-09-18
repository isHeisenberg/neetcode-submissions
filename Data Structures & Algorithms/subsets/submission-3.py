class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if i >= len(nums):
                res.append(sol.copy())  # ricorda di usare copia
                return

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            backtrack(i+1)
            
            return
    
        backtrack(0)    # va usato
        return res