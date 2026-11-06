class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat(k):
            counter = 0
            for pile in piles:
                counter += pile // k
                if pile % k != 0:
                    counter += 1

            return counter <= h
        # F F T T T
        # 1 2 3 4 5 
        while l < r:
            mid = (l + r) // 2
            
            if eat(mid):
                r = mid
            else:
                l = mid + 1

        return l