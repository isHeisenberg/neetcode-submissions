# tra quelli dopo scelgo quello con valore di salto maggiore
# max(posizione + valore): 
# 1,2,4,2,1,0,0 se sono al primo 2, scelgo il 4 pk 4 > 2+1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:   # se la posizione attuale supera il max allora sono fermo
                return False

            max_reach = max(max_reach, i + nums[i]) # aggiorno nuovo massimo

        return True