class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat_k(k):
            hours = 0
            for pile in piles:
                hours = hours + math.ceil(pile / k)
            
            return hours <= h

        while l < r:
            mid = (l + r) // 2
            
            if eat_k(mid):
                r = mid
            else:
                l = mid + 1 


        return l