class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        caratteri = {}
        for i in s:
            caratteri[i] = caratteri.get(i, 0) + 1

        for j in t:
            if caratteri.get(j, 0) == 0:
                return False
            else:
                caratteri[j] = caratteri[j] - 1

        return True
