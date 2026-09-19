class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(dim):
            somma = 0
            counter = 0
            for n in nums:
                somma += n
                if somma > dim:
                    counter += 1
                    somma = n

            return counter + 1 <= k
        
        l, r = max(nums), sum(nums)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res