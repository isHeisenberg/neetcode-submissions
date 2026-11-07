class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1 2 3
        # 1 []
        # 1 12 [] 2
        # 1 13 12 123 [] 3 2 23
        res = []
        sol = []

        def backtrack(i):
            if i >= len(nums):
               res.append(sol.copy())
               return 

            #caso in cui prendo
            sol.append(nums[i])
            backtrack(i+1)
            # caso in cui non prendo
            sol.pop()
            backtrack(i+1)

            return  # risalgo sopra non solo quando in ultimo step!

        backtrack(0)
        return res