'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def add(t1, t2):
            temp = []
            for i in range(3):
                temp.append(max(t1[i], t2[i]))
            return temp

        res = [0, 0, 0]
        for triplet in triplets:
            count = 0
            for j in range(3):
                if target[j] >= triplet[j]:
                    count += 1
            if count == 3:
                res = add(res, triplet)
        return res == target
'''


# + EFFICIENTE
# Set con le posizioni soddisfatte (non triplets) 
# se len == 3, significa che ho soddisfatto tutte le posizioni, quindi fatto!
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3




