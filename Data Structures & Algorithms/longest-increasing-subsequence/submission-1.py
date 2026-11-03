class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

# O(n^2) time
# O(n) memory

'''

# TOP-DOWN
def dfs(i):
    if i == len(s): # base
        return True
    for word in wordDict:
        if s.startswith(word, i):
            if dfs(i + len(word)): # chiama indici maggiori
                return True
    return False
'''