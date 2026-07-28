class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # chiaro controllo sulla lunghezza delle parole
        if len(s) != len(t):
            return False
        
        # così definisco un dizionario (per set devo fare set())
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        
        return True

        # return set(s) == set(t)