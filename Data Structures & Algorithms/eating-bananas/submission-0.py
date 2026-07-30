class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)    # l,r non sono indici, ma valori di rate
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k) # utilizza math.ceil

            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res