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
