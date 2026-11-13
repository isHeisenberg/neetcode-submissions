class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        # fermo se non divisibile per 4
        if total % 4 != 0:
            return False
        edge = total // 4

        # più efficiente se ordine decrescente
        matchsticks.sort(reverse=True)
        # posso fermare subito se c'è uno stick che supera lato
        if matchsticks[0] > edge:
            return False

        n = len(matchsticks)
        used = [False] * n

        def backtrack(idx, k, subsetSum):
            if subsetSum == edge:
                k += 1
                # posso fermarmi a 3, l'altro è ovviamente ok
                if k == 3:
                    return True
                subsetSum = 0
                idx = 0

            for j in range(idx, n):
                if used[j] or subsetSum + matchsticks[j] > edge:
                    continue

                # OTTIMIZZAZIONE
                # skip a stick equal to the previous one if that one is unused
                # if j > 0 and not used[j - 1] and matchsticks[j] == matchsticks[j - 1]:
                #     continue

                used[j] = True
                if backtrack(j + 1, k, subsetSum + matchsticks[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, 0, 0)


