class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        # uso dizionario per ricordare valori e quante volte li ho visitati
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # no bisogno di arg, tanto posso leggere diretto il dict
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return

            for n in counter:
                if counter[n] > 0:
                    sol.append(n)
                    counter[n] -= 1
                    backtrack()

                    counter[n] += 1
                    sol.pop()
                    # backtrack() qui non serve
                    # se lo rifacessi è come se lo facessi con lo stato precedente
                    # in subsets era che simulavo il prendo non prendo, qua no

        backtrack()
        return res 


