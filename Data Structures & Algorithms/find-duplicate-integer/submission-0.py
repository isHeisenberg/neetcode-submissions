class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if (seen[num]) > 1:
                return num