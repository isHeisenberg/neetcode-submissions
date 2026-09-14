# devo trovare la capacità minima utilizzabile
# posso sfruttare BINARY SEARCH: mi serve sapere min, max (cioè l, r!)
# MIN = max peso che ci sta
# MAX = somma di tutti i pesi -> basta un viaggio
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        # mi serve algo che dato una capacità mi scorre su tutti
        def scorro(dim):
            i = 0
            giorni = 0

            while i < len(weights):
                somma = 0
                while i < len(weights) and somma + weights[i] <= dim:
                    somma += weights[i]
                    i += 1

                giorni += 1

            return giorni <= days


        best = 0
        while l <= r:
            mid = (l + r) // 2
            if scorro(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1

        return best



