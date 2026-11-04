class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1 2 2 4 4 5 5 
        # primo quelle che completo da sole
        # poi sx e dx se trovo
        # 1 e 5 done +1
        # 2 2 4 4 5 if 2 + 5 > limit, then r-=1 and 5 in a new boat
        # 2 2 4 4 
        # 2 4
        people.sort()
        l, r = 0, len(people) - 1
        counter = 0
        while l <= r:
            somma = people[l] + people[r]
            if somma <= limit:
                counter += 1
                l += 1
                r -= 1
            else:
                counter += 1
                r -= 1

        return counter

        # 1 3 2 3 2
        # 1 2 2 3 3 -> 1 2 2 3 -> 1 2 2 -> 2


