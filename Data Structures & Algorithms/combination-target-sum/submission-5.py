class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            # questo con solo i mi permette di ripetere dei valori
            dfs(i, cur, total + nums[i])
            cur.pop()
            # qui vado avanti con i numeri
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res



'''
non è tipo subsets in cui si fa sempre i+1
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            backtrack(i+1)
'''