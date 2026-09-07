class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        used = [False] * len(nums)

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True

                sol.append(nums[i])
                backtrack()
                sol.pop()

                used[i] = False

        backtrack()
        return res