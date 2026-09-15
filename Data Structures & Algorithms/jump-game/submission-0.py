class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # tra quelli dopo scelgo quello con valore di salto maggiore
        # max(posizione + valore): 
        # 1,2,4,2,1,0,0 se sono al primo 2, scelgo il 4 pk 4 > 2+1
        i = 0

        while i < len(nums) - 1:
            max_reach = -1
            next_i = i

            # attento: parto da i+1, non i. Inoltre exclusive upper bound
            for j in range(i + 1, i + nums[i] + 1): 
                if j >= len(nums):  # se sforo, allora bene
                    break

                if j + nums[j] > max_reach:    # nuovo massimo di distanza
                    max_reach = j + nums[j]
                    next_i = j

            if next_i == i:     # significa che non mi posso muovere
                return False

            i = next_i

        return True

