class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(sol.copy())
                return

            # se includo nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            val = sol.pop()

            # se non includo nums[i]
            while i < len(nums) and nums[i] == val:
                i += 1
            backtrack(i)

        backtrack(0)
        return res